import pandas as pd 

# creating a DataFrame with a list
mylist = ["C++", "Python", "Java", "C#"]
df1 = pd.DataFrame(mylist)
print("Creating DataFrame from list, df1:"); print(df1)
print("index:"); print(df1.index)
print("values:"); print(df1.values)
print("type of values:"); print(type(df1.values))

# creating a DataFrame with a list and more information
df2 = pd.DataFrame(data=mylist, columns=["course"])
print("\nCreating DataFrame from list, df2:"); print(df2)
print("index:"); print(df2.index)
print("values:"); print(df2.values)
print("type of values:"); print(type(df2.values))
