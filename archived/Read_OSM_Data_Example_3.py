from pyrosm import OSM
from shapely.geometry import Point, Polygon
from matplotlib import pyplot as plt

# 4 points for bounding box
lat_lon = [(48.868486122465455, 2.275354185245491), (48.86907183018768, 2.325959906405398),
           (48.84762395027295, 2.326058842321644), (48.84973985530085, 2.26971483801946)]

# list comprehension
pnt_list = [Point(lon, lat) for (lat, lon) in lat_lon]

# define a polygon as bounding box
bnd_poly = Polygon(pnt_list)

# create a OSM object
osm = OSM(filepath="Paris.osm.pbf", bounding_box=bnd_poly)

# read all POIs
all_pois = osm.get_pois()
print("all_pois tags: ", all_pois.columns)

fig, ax = plt.subplots(1)
all_pois.plot(ax=ax, markersize=2)
ax.set_title("All POIs")
plt.show()

custom_filter = {"amenity": True, "shop": True}
# read POIs with filters
some_pois = osm.get_pois(custom_filter=custom_filter)
print("all_pois tags: ", all_pois.columns)

fig, ax = plt.subplots(1)
some_pois.plot(ax=ax, markersize=2)
ax.set_title("Some POIs")
plt.show()
