from shapely.geometry import LineString, Point
import geopandas as gpd
from matplotlib import pyplot as plt

x1 = 0; y1 = 0
x2 = 1; y2 = 2

# create a Linestring using a list of point coordinates
line1 = LineString([(x1, y1), (x2, y2)])
# create a LineString using a list of pints
line2 = LineString([Point(3, 4), Point(5,6)])

# area property 
print("line1.area: ", line1.area)
# length property
print("line1.length: ", line1.length)
# bounds property
print("line1.bounds: ", line1.bounds)
# coords property
print("line1.coords: ", list(line1.coords))

gs = gpd.GeoSeries(data=[line1, line2])
gs.plot()
plt.show()

