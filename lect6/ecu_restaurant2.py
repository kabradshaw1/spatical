import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from matplotlib import pyplot as plt

# DataFrame
df = pd.read_csv("ecu_restaurants.csv")

# create GeoSeries using Series
geo_points = gpd.points_from_xy(df["lon"], df["lat"], crs="EPSG:4326")

# alternative way of referencing "lon" and "lat" columns 
#geo_points = gpd.points_from_xy(df.lon, df.lat, crs="EPSG:4326")

# create GeoDataFrame using data and geometry
gdf = gpd.GeoDataFrame(data=df, geometry=geo_points)

# save geo_points to a GeoJSON file
gdf.to_file("ecu_restaurant2.geojson", driver="GeoJSON")
gdf.plot()
plt.show()
