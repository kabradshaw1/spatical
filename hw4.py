import geopandas as gpd
import pandas as pd
from matplotlib import pyplot as plt

# Define the paths to your data files
parcels_file_path = 'Data/Beaufort_County_Parcels/parcels.shp'
addresses_file_path = 'Data/Beaufort_Count_Streets/addresses.shp'

# Read the shapefiles
parcels = gpd.read_file(parcels_file_path)
addresses = gpd.read_file(addresses_file_path)

# Convert columns to numeric values (handling errors)
parcels['ACRES'] = pd.to_numeric(parcels['ACRES'], errors='coerce')
parcels['CalcAcres'] = pd.to_numeric(parcels['CalcAcres'], errors='coerce')

# Calculate Acre_Diff
parcels['Acre_Diff'] = parcels['ACRES'] - parcels['CalcAcres']

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
