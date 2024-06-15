import pandas as pd 
import numpy as np 

# create a DataFrame 
df = pd.DataFrame([[1,2]]*3, columns=["A", "B"])
print("\n df: "); print(df)

# apply a numpy function
print("\n apply np.sqrt")
print(df.apply(np.sqrt))

# Lambda function
print("\n apply lambda function")
print(df.apply(lambda x: x*x))

print("\n apply lambda function to column B")
print(df["B"].apply(lambda x: x*x))

