import pandas as pd
arr1 = [10, 20, 30, 40, 50, 60]
arr2 = [10, 20, 30, 40, 50, "60"]

series1 = pd.Series(arr1)
series2 = pd.Series(arr2)

print("series1\n", series1)
print("shape of series1: ", series1.shape)
print("length of series1: ", len(series1)) 
print("series2\n", series2)
print("shape of series2: ", series1.shape)
print("length of series2: ", len(series1)) 
