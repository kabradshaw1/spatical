import pandas as pd

# creating DataFrame with dict 
my_dict1 = {"ID": [100, 101, 102], 
            "Course": ["C++", "Python", "Java"]}
df3 = pd.DataFrame(my_dict1)
print("Creating DataFrame with dict + list, df3:")
print(df3)

# creating DataFrame with Series
my_dict2 = {"ID": pd.Series([100, 101, 102]),
            "Course": pd.Series(["C++", "Python", "Java"])}
df4 = pd.DataFrame(my_dict2)
print("\nCreating DataFrame with dict + Series, df4:")
print(df4)
