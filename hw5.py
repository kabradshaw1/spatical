import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import simplekml

# Load the CSV file
file_path = 'active_verified_pitt.csv'
df = pd.read_csv(file_path)

# Filter voters whose last name starts with 'B'
filtered_df = df[df['last_name'].str.startswith('B')]

# Select the first 10 filtered addresses
sample_df = filtered_df.head(10).copy()

# Initialize geolocator
geolocator = Nominatim(user_agent="voter_geocoder")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Geocode the addresses
sample_df['full_address'] = sample_df['res_street_address'] + ', ' + sample_df['res_city_desc'] + ', ' + sample_df['state_cd'] + ' ' + sample_df['zip_code'].astype(str)
sample_df['location'] = sample_df['full_address'].apply(geocode)

# Debugging: Print geocoded locations
print(sample_df[['full_address', 'location']])

# Extract latitude and longitude
sample_df['latitude'] = sample_df['location'].apply(lambda loc: loc.latitude if loc else None)
sample_df['longitude'] = sample_df['location'].apply(lambda loc: loc.longitude if loc else None)

# Debugging: Print rows with successful geocoding
print(sample_df[['full_address', 'latitude', 'longitude']])

# Initialize KML
kml = simplekml.Kml()

# Create KML points for each voter
for index, row in sample_df.iterrows():
    if pd.notnull(row['latitude']) and pd.notnull(row['longitude']):
        kml.newpoint(name=f"{row['first_name']} {row['middle_name']} {row['last_name']}", 
                     coords=[(row['longitude'], row['latitude'])])

# Save KML file
kml.save("voters.kml")

print("KML file generated successfully.")
