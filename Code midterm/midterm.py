import pandas as pd
import geopandas as gpd
from pathlib import Path
import matplotlib.pyplot as plt
from multiprocessing import Pool
import re

def main():
    # Get the current script's directory
    script_dir = Path(__file__).resolve().parent

    # Resolve the data path relative to the script directory
    data_path = script_dir.parent / 'Data'

    ncvoter7 = data_path / "ncvoter7.txt"

    # Read the file with a fallback encoding
    try:
        df = pd.read_csv(ncvoter7, delimiter='\t', encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(ncvoter7, delimiter='\t', encoding='latin1')

    active_voters_df = df[df['voter_status_desc'] == 'ACTIVE']

    filtered_file_path = script_dir / 'active_voters.csv'
    active_voters_df.to_csv(filtered_file_path, index=False)

    # Read the addresses.shp file into a GeoDataFrame and convert it into WGS 84
    shapefile_path = data_path / "Beaufort_Count_Streets/addresses.shp"
    address_gdf = gpd.read_file(shapefile_path)

    # Save a CSV of the non-geometry data
    address_df = address_gdf.drop(columns=["geometry"])
    address_df.to_csv("beaufort_addresses.csv", index=False)

    # Transform the CRS to WGS 84
    address_4326 = address_gdf.to_crs(epsg=4326)

    geopackage_path = script_dir / 'addresses_4326.gpkg'

    # Remove existing file if it exists to prevent conflicts
    if geopackage_path.exists():
        try:
            geopackage_path.unlink()
        except PermissionError:
            print(f"PermissionError: Unable to delete {geopackage_path}. Ensure you have the correct permissions.")
            return

    # Save the GeoDataFrame to a GeoPackage
    try:
        address_4326.to_file(geopackage_path, driver='GPKG')
    except Exception as e:
        print(f"Error saving GeoPackage: {e}")
        return

def clean_address(address: str) -> str:
    # Replace multiple spaces with a single space
    return re.sub(r'\s+', ' ', address).strip()

def match_address(add_str: str, add_series: pd.Series):
    for i in add_series.index:
        add_gpd = add_series.loc[i]
        if add_str.upper() in add_gpd.upper():
            return i
    return None

if __name__ == '__main__':
    main()

    active_voter = pd.read_csv("active_voters.csv")
    add_list = active_voter["res_street_address"].apply(clean_address).to_list()

    # Read the addresses GeoPackage to get address
    address_gpd = gpd.read_file("./addresses_4326.gpkg")
    full_address_series = address_gpd["FullAddres"]

    # Prepare input list for multiprocessing
    input_list = [(add_str, full_address_series) for add_str in add_list]

    with Pool(12) as process_pool:
        returned_index_list = process_pool.starmap(func=match_address, iterable=input_list)

    final_add_list = []
    final_pnt_list = []

    for add_idx, gpd_idx in enumerate(returned_index_list):
        if gpd_idx is not None:
            final_add_list.append(add_list[add_idx])
            final_pnt_list.append(address_gpd.loc[gpd_idx, "geometry"])

    add_geo_pd = pd.DataFrame(data={"StreetAddress": final_add_list, "geometry": final_pnt_list})
    add_geo_gpd = gpd.GeoDataFrame(data=add_geo_pd, geometry="geometry")

    # Save matched addresses to a GeoPackage
    matched_geopackage_path = Path('matched_addresses.gpkg')

    # Remove existing file if it exists to prevent conflicts
    if matched_geopackage_path.exists():
        try:
            matched_geopackage_path.unlink()
        except PermissionError:
            print(f"PermissionError: Unable to delete {matched_geopackage_path}. Ensure you have the correct permissions.")
        except Exception as e:
            print(f"Error removing existing matched_addresses.gpkg: {e}")

    try:
        add_geo_gpd.to_file(matched_geopackage_path, driver='GPKG')
    except Exception as e:
        print(f"Error saving matched addresses GeoPackage: {e}")

    # Plot the matched addresses
    add_geo_gpd.plot()
    plt.show()
