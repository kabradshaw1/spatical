import pandas as pd
mydict = {"Name":["John", "Jack", "Tom", "Bob"],
          "Math":[98, 95, 91, 93], 
          "Science":[97, 90, 98, 95]}
df = pd.DataFrame(mydict)
print("\n df:"); print(df)
# using loc and list
df.loc[len(df)]=["Alex", 92, 99]
print("\n add a new row with loc, now df:"); print(df)

# using append and dict, deprecated function
mydict = {"Name": "Amy", "Math": 100, "Science": 99}
df._append(mydict, ignore_index=True) # ignore_index has to be True
print("\n append a new row using dict, now df:"); print(df)

# using concate function
df2 = pd.concat([df, df]) # concate takes list as input 
print("\n concate df to df, df2:"); print(df2) 


