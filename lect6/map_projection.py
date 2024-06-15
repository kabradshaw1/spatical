import geopandas as gpd
from matplotlib import pyplot as plt

usa_file_path="geodata/natregimes.gpkg"
fig, axes = plt.subplots(3,1)

usa1 = gpd.read_file(usa_file_path)
usa1.plot(ax=axes[0])
axes[0].set_title("EPSG:4328-WGS 84")

usa2 = usa1.to_crs("EPSG:3857")
usa2.plot(ax=axes[1])
axes[1].set_title("EPSG:3857 – Web Mercator Projection")

usa3 = usa1.to_crs("ESRI:102003")
usa3.plot(ax=axes[2]); 
axes[2].set_title("NAD 1983 Albers contiguous USA")

print("usa1 CRS:\n", repr(usa1.crs)) # what is "repr"? 
print("usa2 CRS:\n", repr(usa2.crs)) 
print("usa2 CRS:\n", repr(usa2.crs))
plt.show()
