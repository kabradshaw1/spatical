import pyrosm
from pathlib import Path
from matplotlib import pyplot as plt

# Let's use "Path" here
nc_data_folder = Path("./NC_Data/")
nc_osm_file = nc_data_folder / "north-carolina-latest.osm.pbf"
osm = pyrosm.OSM(str(nc_osm_file))

# read the boundary of Pitt County
pitt_bnd = osm.get_boundaries(name="Pitt County")
pitt_bnd.to_file("./pitt_bnd.gkpg", driver="GPKG")
fig, ax = plt.subplots(1)
pitt_bnd.plot(ax=ax)
ax.set_title("Pitt County Boundary")
plt.show()

