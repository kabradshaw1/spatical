import pandas as pd
import numpy as np
from datetime import datetime
months=["January", "February", "March", "April",
"May", "June", "July", "August",
"September", "October", "November", "December"]
df = pd.read_csv("NCEL_Mega-Millions.csv")
print("\n NC Mega Millions Record:"); print(df)
# subset DataFrame
df_numbers = df.filter(items=['Number 1', 'Number 2', 'Number 3',
'Number 4', 'Number 5', 'Megaball'])
print("\ndf_numbers:"); print(df_numbers)
# convert "Date" column from "str" into "datetime"
# lambda function
df_date = df["Date"].apply(lambda x: datetime.strptime(x,"%m/%d/%Y"))
print("\n df_date:"); print(df_date)
# join two data frames, "inner"/"outer" join
df2 = pd.concat([df_date, df_numbers], axis=1, join="inner")
print("\n inner join of df_numbers and df_date, df2:"); print(df2)
# subset DataFrame using boolean indexing
index_2023 = (df2["Date"] <datetime(2024,1, 1)) & (df2["Date"] >datetime(2023,1,
1))
df_2023 = df2[index_2023]
print("\n df_2023:"); print(df_2023)
