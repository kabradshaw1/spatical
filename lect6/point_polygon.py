from shapely.geometry import Polygon, Point
import geopandas as gpd
from matplotlib import pyplot as plt

x1 = 1; y1 = 0
x2 = 0; y2 = 1
x3 = -1; y3 = 0
x4 = 0; y4 = -1

# create a Polygon using a list of point coordinates
polygon1 = Polygon([(x1, y1), (x2, y2), (x3, y3), (x4, y4)])

p0 = Point(0, 0)
p5 = Point(5, 5)

print("\npolygon1 contains p0? ", polygon1.contains(p0))
print("\np0 within polygon1? ", p0.within(polygon1))
print("\npolygon1 contains p5? ", polygon1.contains(p5))
print("\np5 within polygon1? ", p5.within(polygon1))

# GeoSeries with mixed type 
gs = gpd.GeoSeries(data=[polygon1, p0, p5])
# plot GeoSeries with settings 
gs.plot(facecolor="none", edgecolor="red", lw=1)
plt.show()

