import geopandas as gpd
from matplotlib import pyplot as plt

# read address from shapefile
# there are about 7 files in a shape file folder, please read the file with ".shp" extension
address = gpd.read_file("Data/Beaufort_Count_Streets/addresses.shp")
print("address CRS: ", address.crs)
print("address geometry: ", address["geometry"])

# read road from shapefile
road = gpd.read_file("Data/Beaufort_Count_Streets/centerlines.shp")
print("road CRS: ", road.crs)
print("road geometry: ", road["geometry"])

# read parcels from shapefile
parcel = gpd.read_file("Data/Beaufort_County_Parcels/parcels.shp")
print("parcel CRS: ", parcel.crs)
print("parcel geometry: ", parcel["geometry"])

fig, ax = plt.subplots(1)
parcel.plot(ax=ax)  # try edge_color="black", fillcolor="none", "linewidth=0.5)
road.plot(ax=ax)    # try linewidth
address.plot(ax=ax, markersize=0.2, color="r")
plt.show()
