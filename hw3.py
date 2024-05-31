import pandas as pd
import numpy as np

"""
Read the CSV file. This requires the CSV file to 
be in the same directory as this script.
"""
file_path = "NCEL_Mega-Millions.csv"
df = pd.read_csv(file_path)

# Convert 'Date' to datetime format. The dates in the CSV file are strings.
df['Date'] = pd.to_datetime(df['Date'])

# Filter data for 2023
df_2023 = df[df['Date'].dt.year == 2023]

# Find the most frequent winning numbers in 2023 using lambda function
most_frequent_2023 = df_2023[['Number 1', 'Number 2', 'Number 3', 'Number 4', 'Number 5', 'Megaball']].apply(lambda x: x.mode().iloc[0])

# Filter data for June in all years
df_june = df[df['Date'].dt.month == 6]

# Function to find most and least frequent numbers
def find_frequencies(column):
    values, counts = np.unique(column, return_counts=True)
    return values[np.argmax(counts)], values[np.argmin(counts)]

# Find the most and least frequent winning numbers in June using lambda function
most_frequent_june = df_june[['Number 1', 'Number 2', 'Number 3', 'Number 4', 'Number 5', 'Megaball']].apply(lambda x: find_frequencies(x)[0])
least_frequent_june = df_june[['Number 1', 'Number 2', 'Number 3', 'Number 4', 'Number 5', 'Megaball']].apply(lambda x: find_frequencies(x)[1])

# Print the results
print("Most frequent winning numbers in 2023:")
for col, num in most_frequent_2023.items():
    print(f"{col}: {num}")

print("\nMost frequent winning numbers in June:")
for col, num in most_frequent_june.items():
    print(f"{col}: {num}")

print("\nLeast frequent winning numbers in June:")
for col, num in least_frequent_june.items():
    print(f"{col}: {num}")
