import geopandas as gpd
from pathlib import Path

# read the geopackage file
print("read data")
data_path = Path("../Output")
all_voters_gpkg_file = data_path / "all_voters_method_1.gpkg"
all_voters_gdf = gpd.read_file(all_voters_gpkg_file)

# subset the voters according to party group
print("subset data by party group")
dem_voters = all_voters_gdf[all_voters_gdf["party_cd"] == "DEM"]
rep_voters = all_voters_gdf[all_voters_gdf["party_cd"] == "REP"]
una_voters = all_voters_gdf[all_voters_gdf["party_cd"] == "UNA"]

# save the data
print("save data into files")
dem_gpkg_file = data_path / "dem_voters.gpkg"
dem_voters.to_file(dem_gpkg_file, driver="GPKG")

rep_gpkg_file = data_path / "rep_voters.gpkg"
rep_voters.to_file(rep_gpkg_file, driver="GPKG")

una_gpkg_file = data_path / "una_voters.gpkg"
una_voters.to_file(una_gpkg_file, driver="GPKG")
