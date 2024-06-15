from shapely import wkt
import geopandas as gpd
from matplotlib import pyplot as plt

polygon1 = wkt.loads("POLYGON ((0 0, 0 -1, 7.5 -1, 7.5 0, 0 0))")
polygon2 = wkt.loads("POLYGON ((0 1, 1 0, 2 0.5, 3 0, 4 0, 5 0.5, 6 -0.5, 7 -0.5, 7 1, 0 1))")

# why """? """ or ''' tells Python interpreter that the string spans several lines
multi_poly = wkt.loads("""MULTIPOLYGON (((40 40, 20 45, 45 30, 40 40)), 
                                        ((20 35, 10 30, 10 10, 30 5, 45 20, 20 35), 
                                         (30 20, 20 15, 20 25, 30 20)))""")
print("type of polygon1: ", type(polygon1))
print("type of multi_poly: ", type(multi_poly))
gdf = gpd.GeoSeries(data=[polygon1, polygon2, multi_poly])
gdf.plot()
plt.show()

