import pandas as pd
mydict = {"Name":["John", "Jack", "Tom", "Bob", "Amy"],
          "Math":[98, 95, 91, 93, 100], 
          "Science":[97, 90, 98, 95, 100]}
df = pd.DataFrame(mydict)

# using concate function
df2 = pd.concat([df, df]) # concate takes list as input 
print("\n concate df to df, df2:"); print(df2) 

# drop duplicates
df2.drop_duplicates(inplace=True)
print("\n df2 after dropping duplicates:"); print(df2)

# drop a row using index 
df3 = df2.drop(3)
print("\n df3 is df2 after drop index `3`");print(df3)

# drop rows according to condition
df4 = df2.drop(df[df.Math<95].index)
print("\n df4 is df2 dropping rows whose Math < 95"); print(df4)
