import pyrosm
from matplotlib import pyplot as plt
import geopandas as gpd

# read Pitt Count boundary
pitt_bnd = gpd.read_file("./pitt_bnd.gpkg")

# read Pitt County parcel data
# (1) read the NC osm data with a bounding box
bnd_poly = pitt_bnd.loc[0, "geometry"]
# bnd_poly: <POLYGON ((-77.7 35.7, -77.7 35.7, -77.7 35.7, -77.7 35.7, -77.7 35.6, -77.7...>
pitt_osm = pyrosm.OSM(filepath="./NC_Data/north-carolina-latest.osm.pbf", bounding_box=bnd_poly)

# (2) get the buildings 
pitt_parcel = pitt_osm.get_buildings()
pitt_parcel.to_file("pitt_buildings.gpkg",driver="GPKG") 
fig, ax = plt.subplots(1)
pitt_parcel.plot(ax=ax)
ax.set_title("Pitt County Buildings")
plt.show()
