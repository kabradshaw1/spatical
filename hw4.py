import geopandas as gpd
from matplotlib import pyplot as plt
import os

# Define the paths to the data files
parcels_file_path = 'Data/Beaufort_County_Parcels/parcels.shp'
addresses_file_path = 'Data/Beaufort_Count_Streets/addresses.shp'

# Verify that the files exist
if not os.path.exists(parcels_file_path):
    raise FileNotFoundError(f"The file at path '{parcels_file_path}' does not exist.")
if not os.path.exists(addresses_file_path):
    raise FileNotFoundError(f"The file at path '{addresses_file_path}' does not exist.")

# Read the shapefiles
parcels = gpd.read_file(parcels_file_path)
addresses = gpd.read_file(addresses_file_path)

# Calculate Acre_Diff
parcels['Acre_Diff'] = parcels['Acre_5070'] - parcels['CalcAcres']

# Filter parcels based on Acre_Diff
filtered_parcels = parcels[(parcels['Acre_Diff'] > 3.0) & (parcels['Acre_Diff'] < 4.0)]

# Perform a spatial join to find addresses within the identified parcels
addresses_within_parcels = gpd.sjoin(addresses, filtered_parcels, how='inner', op='within')

# Plot the parcels and addresses
fig, ax = plt.subplots(figsize=(10, 10))
base = filtered_parcels.plot(ax=ax, edgecolor='black', color='none')
addresses_within_parcels.plot(ax=base, marker='+', color='red', markersize=50)

plt.title('Addresses within Parcels with 3.0 < Acre_Diff < 4.0')
plt.savefig('addresses_within_parcels.jpg')
plt.show()
