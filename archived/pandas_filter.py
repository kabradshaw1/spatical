import numpy as np
import pandas as pd

df1 = pd.DataFrame(data=np.array([[2, 3, 4], [5, 6, 7]]),
                  index=["dog", "cat"],
                  columns=["room1", "room2", "room3"])
print("\n DataFrame from array, df1:"); print(df1)

# select columns by name
df2 = df1.filter(items=["room1", "room3"])
print("\n filter with items, df2:"); print(df2)

# select columns by regular expression
# 'axis = 1' => column
df3 = df1.filter(regex="3$", axis=1)
print("\n filter with regular expression, for column: df3")
print(df3)

# select rows by like expression
# 'aixs = 0' => row
df4 = df1.filter(like="d", axis=0)
print("\n filter with like expression, for rows: df4")
print(df4)
