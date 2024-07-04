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
# Create a rate limiter with at least a 1 second delay between requests
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Function to geocode an address
def geocode_address(row):
    address = f"{row['res_street_address']}, {row['res_city_desc']}, {row['state_cd']} {int(row['zip_code'])}"
    try:
        location = geocode(address)
        if location:
            return row['first_name'], row['middle_name'], row['last_name'], location.latitude, location.longitude
        else:
            return row['first_name'], row['middle_name'], row['last_name'], None, None
    except Exception as e:
        print(f"Error geocoding {address}: {e}")
        return row['first_name'], row['middle_name'], row['last_name'], None, None

# Process geocoding with early stop after 10 successful geocodes
def process_geocoding(rows):
    results = []
    for _, row in rows.iterrows():
        result = geocode_address(row)
        if result[3] is not None and result[4] is not None:
            results.append(result)
            if len(results) >= 10:
                break
    return results

# Apply the geocoding function to the filtered voters
geocoded_results = process_geocoding(filtered_df)

# Initialize KML
kml = simplekml.Kml()

# Add points to KML
for first_name, middle_name, last_name, latitude, longitude in geocoded_results:
    name = f"{first_name} {middle_name} {last_name}".strip()
    kml.newpoint(name=name, coords=[(longitude, latitude)])

# Save the KML file
kml.save("voter_locations.kml")

print("Geocoding and KML generation complete.")
