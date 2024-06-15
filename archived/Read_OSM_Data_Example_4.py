from pyrosm import OSM
from matplotlib import pyplot as plt

# create a OSM object
osm = OSM(filepath="Paris.osm.pbf")

# default boundary
boundaries = osm.get_boundaries()
print("boundary columns: \n", boundaries.columns)
print("boundary names: \n", set(boundaries["name"]))
fig, ax = plt.subplots(1)
boundaries.plot(ax=ax, facecolor=None, edgecolor="red")
ax.set_title("default boundaries")
plt.show()

# boundary by type
pb = osm.get_boundaries(boundary_type="political")
fig, ax = plt.subplots(1)
pb.plot(ax=ax, facecolor=None, edgecolor="red")
ax.set_title("political boundaries")
plt.show()
