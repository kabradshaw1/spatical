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

# read landuse data
landuse = osm.get_landuse()
# read natural data
natural = osm.get_natural()

fig, axes = plt.subplots(nrows=2, ncols=1)
landuse.plot(ax=axes[0], column="landuse", legend=True)
axes[0].set_title("Land Use")
natural.plot(ax=axes[1], column="natural", legend=True)
axes[1].set_title("Natural")
plt.show()

