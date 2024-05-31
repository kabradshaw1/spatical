import numpy as np
import pandas as pd 

# creating Series from a list 
mylist = ["East", "Carolina", "University"]
s0 = pd.Series(mylist)
print("\nfrom list, s0:"); print(s0)
print("Shape:", s0.shape); print("Size:", s0.size)
print("Index:", s0.index); print("Dimension:", s0.ndim)
print("Values:", s0.values)

# creating Series from a dictionary
mydict = {"a": "East", "b": "Carolina", "c": "University"}
s2 = pd.Series(mydict)
print("\nfrom dictionary, s2:"); print(s2)
print("Shape:", s2.shape); print("Size:", s2.size)
print("Index:", s2.index); print("Dimension:", s2.ndim)
print("Values:", s2.values)

