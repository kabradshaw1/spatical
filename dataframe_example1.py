import pandas as pd 

# creating empty DataFrame
df0 = pd.DataFrame()
print("Empty DataFrame df0:"); print(df0)
index=["a", "b", "c"]
fruit=["Apple", "Banana", "Cherry"]
price=[2.5, 0.9, 3.5]
# assign index 
df0.index = index
# add a column "fruit"
df0["fruit"] = fruit
# add a column "price"
df0["price"] = price 
print("updated df0"); print(df0)
print("index:"); print(df0.index)
print("values:"); print(df0.values)
print("type of values:"); print(type(df0.values))
