from shapely.geometry import Point
import geopandas as gpd
from matplotlib import pyplot as plt

x1 = 0; y1 = 0
x2 = 1; y2 = 2

p1 = Point(x1, y1)
p2 = Point(x2, y2)

# area property 
print("p1.area: ", p1.area)
# length property
print("p1.length: ", p1.length)
# bounds property
print("p1.bounds: ", p1.bounds)
# coords property
print("p1.coords: ", list(p1.coords))
# x, y properties 
print("p1.x = ", p1.x, " p1.y = ", p1.y)

gs = gpd.GeoSeries(data=[p1, p2])
gs.plot()
plt.show()
