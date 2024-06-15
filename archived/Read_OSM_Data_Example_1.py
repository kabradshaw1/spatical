from pyrosm import OSM
from matplotlib import pyplot as plt

# print the help information for constructing a OSM object
help(OSM.__init__)

osm = OSM(filepath="Paris.osm.pbf")
drive_net = osm.get_network(network_type="driving")
print("Data type of drive_net: ", type(drive_net))
drive_net.plot()
plt.show()
