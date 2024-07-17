import matplotlib
import pandas as pd
import numpy as np

df = pd.read_csv('WOFF Database.csv', sep=',')
df['Weight'] = df['Weight'].convert_dtypes(int) #Empty spaces in weight should probably be set to 0 in future. Makes this a string column.
print(df)

median = df['HP Growth'].median()
print("Median HP Growth: " + str(median))