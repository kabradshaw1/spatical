import geopandas as gpd
import matplotlib.pyplot as plt

# Load the parcels GeoDataFrame (assuming the file is named 'beaufort_parcels.geojson')
parcels = gpd.read_file('path/to/beaufort_parcels.geojson')

# Calculate Acre_Diff
parcels['Acre_Diff'] = parcels['Acre_5070'] - parcels['CalcAcres']

# Filter parcels based on Acre_Diff
filtered_parcels = parcels[(parcels['Acre_Diff'] > 3.0) & (parcels['Acre_Diff'] < 4.0)]

# Load the addresses GeoDataFrame (assuming the file is named 'beaufort_addresses.geojson')
addresses = gpd.read_file('path/to/beaufort_addresses.geojson')

# Perform a spatial join to find addresses within the identified parcels
addresses_within_parcels = gpd.sjoin(addresses, filtered_parcels, how='inner', op='within')

# Plot the parcels and addresses
fig, ax = plt.subplots(figsize=(10, 10))
base = filtered_parcels.plot(ax=ax, edgecolor='black', color='none')
addresses_within_parcels.plot(ax=base, marker='+', color='red', markersize=50)

plt.title('Addresses within Parcels with 3.0 < Acre_Diff < 4.0')
plt.savefig('addresses_within_parcels.jpg')
plt.show()
