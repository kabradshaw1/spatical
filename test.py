import geopandas as gpd
import os

# Define the paths to your data files
parcels_file_path = '/Users/kylebradshaw/repos/spatial/Data/Beaufort_County_Parcels/parcels.shp'
addresses_file_path = '/Users/kylebradshaw/repos/spatial/Data/Beaufort_Count_Streets/addresses.shp'

# Verify that the files exist
if not os.path.exists(parcels_file_path):
    raise FileNotFoundError(f"The file at path '{parcels_file_path}' does not exist.")
if not os.path.exists(addresses_file_path):
    raise FileNotFoundError(f"The file at path '{addresses_file_path}' does not exist.")

# Read the shapefiles
parcels = gpd.read_file(parcels_file_path)
addresses = gpd.read_file(addresses_file_path)

# Print columns to inspect the DataFrame
print("Parcels DataFrame Columns:", parcels.columns)
print("First few rows of Parcels DataFrame:\n", parcels.head())

print("Addresses DataFrame Columns:", addresses.columns)
print("First few rows of Addresses DataFrame:\n", addresses.head())
