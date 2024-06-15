from pyrosm.data import sources
from pyrosm import get_data

# (1) understand the hierarchical structure of data source
categories = sources.available.keys()
print("Available categories: \n", categories)
print("North America list: \n", sources.north_america.available)
print("USA list:\n", sources.north_america.usa.available)
print("Variables of usa:\n", vars(sources.north_america.usa))
print("North carolina PBF entry:\n", sources.north_america.usa.north_carolina)

# (2) explore cities
print("Available cities:\n", sources.cities.available)
print("Variables of cities: \n", vars(sources.cities))
print("Paris:\n", sources.cities.paris)

# (3) download Paris data
# If you have downloaded the data previously into your computer, pyrosm will by default use that same data file.
# However, if you want to update the data, it is possible to specify update=True which will remove the old PBF file
# and download a fresh version from Geofabrik or BBBike.
fp = get_data("Paris")
print(fp)