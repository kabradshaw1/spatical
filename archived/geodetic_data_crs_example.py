import geopandas as gpd
from matplotlib import pyplot as plt

gdf = gpd.read_file("./Data/Geodetic_Data/Geodetic_Control_Points.gpkg")
print("current CRS: ", gdf.crs)

# World Geodetic System 1984
gdf_4326 = gdf.to_crs("EPSG:4326")

# Albers Equal Area Projection (EPSG code 9822)
gdf_9822 = gdf_4326.to_crs("EPSG:9822")

# create a plot with 1 row and 3 columns
fig, axes = plt.subplots(nrows=1, ncols=3)

# draw plot on axes[0], what is a markersize?
gdf.plot(ax=axes[0], markersize=0.1)
axes[0].set_title("Original CRS: %s"%(gdf.crs))

# draw plot on axes[1]
gdf_4326.plot(ax=axes[1], markersize=0.1)
axes[1].set_title("EPSG:4326")

# draw plot on axes[2]
gdf_9822.plot(ax=axes[2], markersize=0.1)
axes[2].set_title("EPSG:9822")
plt.show()