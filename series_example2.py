import numpy as np
import pandas as pd 

# creating Series from a list 
mylist = ["East", "Carolina", "University"]
s0 = pd.Series(mylist)
print("\nfrom list, s0:"); print(s0)

# creating Series from an Array
myarray = np.array(["East", "Carolina", "University"])
s1 = pd.Series(myarray)
print("\nfrom array, s1:"); print(s1)

# creating Series from a dictionary
mydict = {"a": "East", "b": "Carolina", "c": "University"}
s2 = pd.Series(mydict)
print("\nfrom dictionary, s2:"); print(s2)

# creating Series from a scalar
s3 = pd.Series(6, index=[1, 2, 3, 4, 5])
print("\n from scalar, s3:"); print(s3) 

