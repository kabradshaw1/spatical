import geopandas as gpd
from matplotlib import pyplot as plt

# read data
address = gpd.read_file("Data/Beaufort_Count_Streets/addresses.shp")
parcel = gpd.read_file("Data/Beaufort_County_Parcels/parcels.shp")

# match first 100 address with parcels
add100 = address[0:100]

# create an empty parcel index list
parcel_idx = []

# find matches
for i in add100.index:
    for j in parcel.index:
        if add100.loc[i, "geometry"].within(parcel.loc[j, "geometry"]):
            parcel_idx.append(j)
            break

print("matched parcel index:", parcel_idx)

# save into GeoPackage files
add100.to_file("address_100.gpkg", driver="GPKG")
parcel100 = parcel.loc[parcel_idx]
parcel100.to_file("parcel_100.gpkg", driver="GPKG")

fig, ax = plt.subplots(1)
parcel100.plot(ax=ax, facecolor="none")
add100.plot(ax=ax, marker="+", markersize=10, color="r")
plt.show()
