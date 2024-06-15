import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from matplotlib import pyplot as plt

# DataFrame
df = pd.read_csv("ecu_restaurants.csv")
points = []
for i in df.index:
    x = df.loc[i, "lon"]
    y = df.loc[i, "lat"]
    
    # what does 10.8 mean? 
    print("lon=%10.8f lat=%10.8f"%(x, y))
    pnt = Point((x, y))
    points.append(pnt)

print("\n points:"); print(points)
# create GeoSereis using a list
geo_points = gpd.GeoSeries(data=points, crs="EPSG:4326")
print("\n geo_points:"); print(geo_points)

# save geo_points to a GeoJSON file
geo_points.to_file("ecu_restaurant.geojson", driver="GeoJSON")
geo_points.plot()
plt.show()
