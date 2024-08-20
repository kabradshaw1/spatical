import geopandas as gpd
from pathlib import Path

def count_matched_addresses():
    # Define the path to the GeoPackage file
    matched_geopackage_path = Path('matched_addresses.gpkg')

    # Check if the file exists
    if not matched_geopackage_path.exists():
        print(f"The file {matched_geopackage_path} does not exist.")
        return

    # Read the GeoPackage file
    try:
        matched_addresses_gdf = gpd.read_file(matched_geopackage_path)
    except Exception as e:
        print(f"Error reading GeoPackage: {e}")
        return

    # Get the number of records
    num_matches = len(matched_addresses_gdf)
    print(f"Number of matched addresses: {num_matches}")

if __name__ == '__main__':
    count_matched_addresses()
