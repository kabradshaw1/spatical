import geopandas as gpd
import time

# read GeoJSON format file into a GeoDataFrame
start = time.time()
control_points_1 = gpd.read_file("./Data/Geodetic_Data/Geodetic_Control_Points.geojson")
end = time.time()
print("reading GeoJSON file takes %s seconds"%(end-start))


# read Shapefile format file
start = time.time()
control_points_2 = gpd.read_file("./Data/Geodetic_Data/Geodetic_Control_Points/Geodetic_Control_Points.shp")
end = time.time()
print("reading Shapefile takes %s seconds"%(end-start))

# write GeoDataFrame into a GeoPackage file
control_points_2.to_file("./Data/Geodetic_Data/Geodetic_Control_Points.gpkg", driver="GPKG")

# read Shapefile format file
start = time.time()
control_points_2 = gpd.read_file("./Data/Geodetic_Data/Geodetic_Control_Points.gpkg")
end = time.time()
print("reading GeoPackage file takes %s seconds"%(end-start))
