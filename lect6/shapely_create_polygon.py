from shapely.geometry import Polygon, Point
import geopandas as gpd
from matplotlib import pyplot as plt

x1 = 0; y1 = 0
x2 = 1; y2 = 2
x3 = 2; y3 = 3

# create a Polygon using a list of point coordinates
polygon1 = Polygon([(x1, y1), (x2, y2), (x3, y3)])
# create a Polygon using a list of pints
polygon2 = Polygon([Point(3, 4), Point(5,6), Point(-1, 4)])

# area property 
print("polygon1.area: ", polygon1.area)
# length property
print("polygon1.length: ", polygon1.length)
# bounds property
print("polygon1.bounds: ", polygon1.bounds)
# centroid property
print("polygon1.centroid: ", polygon1.centroid)

gs = gpd.GeoSeries(data=[polygon1, polygon2])
gs.plot()
plt.show()

