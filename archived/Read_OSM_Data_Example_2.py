from pyrosm import OSM
from shapely.geometry import Point, Polygon
from matplotlib import pyplot as plt

# Go to Google Map and grap lat/lon coordinates for 4 points
# in Google Map, right click mouse to copy latitude, longitude coordinates
lat_lon = [(48.868486122465455, 2.275354185245491), (48.86907183018768, 2.325959906405398),
           (48.84762395027295, 2.326058842321644), (48.84973985530085, 2.26971483801946)]
# list comprehension
pnt_list = [Point(lon, lat) for (lat, lon) in lat_lon]

# define a polygon as bounding box
bnd_poly = Polygon(pnt_list)

# create a OSM object
osm = OSM(filepath="Paris.osm.pbf", bounding_box=bnd_poly)

# read driving network
drive_net = osm.get_network(network_type="driving")
print("Data type of drive_net: ", type(drive_net))
fig, ax = plt.subplots(1)
drive_net.plot(ax=ax)
ax.set_title("Driving Network")
plt.show()

# read building
buildings = osm.get_buildings()
print("buildings variables: \n", buildings.columns)
fig, ax = plt.subplots(1)
buildings.plot(ax=ax)
ax.set_title("Building footprints")
plt.show()

