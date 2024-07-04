import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import simplekml
import time

# Load the CSV file
file_path = './active_verified_pitt.csv'
df = pd.read_csv(file_path)

# Filter voters with last names starting with 'B'
filtered_df = df[df['last_name'].str.startswith('B')]

# Select the first 10 voters for the task
sample_voters = filtered_df.head(10).copy()  # Use .copy() to avoid the SettingWithCopyWarning

# Initialize the geocoder
geolocator = Nominatim(user_agent="voter_geocoder")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Function to geocode an address
def geocode_address(row):
    address = f"{row['res_street_address']}, {row['res_city_desc']}, {row['state_cd']} {int(row['zip_code'])}"
    try:
        location = geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except Exception as e:
        print(f"Error geocoding address {address}: {e}")
        return None, None

# Apply the geocoding function to the sample voters
sample_voters.loc[:, ['latitude', 'longitude']] = sample_voters.apply(geocode_address, axis=1, result_type='expand')

# Initialize KML
kml = simplekml.Kml()

# Add points to KML
for _, row in sample_voters.iterrows():
    if pd.notnull(row['latitude']) and pd.notnull(row['longitude']):
        name = f"{row['first_name']} {row['middle_name']} {row['last_name']}".strip()
        kml.newpoint(name=name, coords=[(row['longitude'], row['latitude'])])

# Save the KML file
kml.save("voter_locations.kml")

print("Geocoding and KML generation complete.")
