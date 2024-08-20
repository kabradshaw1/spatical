import geopandas as gpd
from pathlib import Path
from matplotlib import pyplot as plt


data_path = Path("../Data")

address_shp_file = data_path / "Beaufort_Count_Streets/addresses.shp"
print("type of address_shp_file: ", type(address_shp_file))

# making this shp file a variable that we can apply these other methods to
address_gdf = gpd.read_file(address_shp_file)

# dropping the geometry column to convert the GeoDataFrame into a DataFrame
address_df = address_gdf.drop(columns=["geometry"])
address_df.to_csv("beaufort_address.csv")

# outputting the DataFrame into a CSV file
address_gdf.to_csv("beaufort_address_gdf.csv")
print("CRS: ", address_gdf.crs)

address_4326 = address_gdf.to_crs(epsg=4326)

address_4326.to_csv("address_4326.csv")
address_4326.to_file("address_4326.gpkg", driver="GPKG")
