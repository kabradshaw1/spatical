import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import simplekml

# Load the CSV file
file_path = './active_verified_pitt.csv'
df = pd.read_csv(file_path)

# Filter voters with last names starting with 'B'
filtered_df = df[df['last_name'].str.startswith('B')]

# Initialize the geocoder
geolocator = Nominatim(user_agent="voter_geocoder")
# Adjust the rate limiter settings
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=2, max_retries=3, error_wait_seconds=5)

# Function to geocode an address
def geocode_address(row):
    address = f"{row['res_street_address']}, {row['res_city_desc']}, {row['state_cd']} {int(row['zip_code'])}"
    try:
        location = geocode(address, timeout=10)  # Increase timeout duration
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except Exception as e:
        print(f"Error geocoding address {address}: {e}")
        return None, None

# Collect geocoded addresses until we have 10 valid locations
valid_locations = []
for _, row in filtered_df.iterrows():
    if len(valid_locations) >= 10:
        break
    latitude, longitude = geocode_address(row)
    if latitude is not None and longitude is not None:
        valid_locations.append({**row, 'latitude': latitude, 'longitude': longitude})

# Convert valid locations to DataFrame
sample_voters = pd.DataFrame(valid_locations)

# Initialize KML
kml = simplekml.Kml()

# Add points to KML
for _, row in sample_voters.iterrows():
    name = f"{row['first_name']} {row['middle_name']} {row['last_name']}".strip()
    kml.newpoint(name=name, coords=[(row['longitude'], row['latitude'])])

# Save the KML file
kml.save("voter_locations.kml")

print("Geocoding and KML generation complete.")
