import pandas as pd

# creating DataFrame with dict 
my_dict = {"ID": [100, 101, 102], 
            "Course": ["C++", "Python", "Java"]}
df = pd.DataFrame(my_dict)
# access column "ID"
print("\nID:"); print(df["ID"])
# access column "Course"
print("\nCourse:"); print(df["Course"])

# add a new column with list
df["Credit"] = [4, 3, 3]
print("\nCredit:"); print(df["Credit"])

# add a new column with Series
df["Room"] = pd.Series(["E401", "E302", "E200"])
print("\nRoom:"); print(df["Room"]) 

# delete a column from DataFrame
df.pop("Credit")
print("\nDataFrame:"); print(df) 
