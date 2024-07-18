import matplotlib
import pandas as pd
import numpy as np

df = pd.read_csv('WOFF Database.csv', sep=',')
df['Weight'] = df['Weight'].convert_dtypes(int) #Empty spaces in weight should probably be set to 0 in future. Makes this a string column.
print(df)

#Replace null Weights with 0
#Replace null Prismunity with None
#Next test average number of Mirages vs Location
#Test AGI Growth vs Size
highMagic = df.loc[df['MAG Growth'] >=4]
LowMagic = df.loc[df['MAG Growth'] < 4]
highMagic.reset_index(drop=True, inplace=True)
LowMagic.reset_index(drop=True, inplace=True)



print(highMagic)
print(LowMagic)
print(highMagic['Size'].value_counts(normalize=True)) #Average Sizes for High Magic Mirages
# L     0.450549
# M     0.230769
# S     0.186813
# XL    0.131868
print(highMagic['HP Growth'].value_counts())
print(LowMagic['STR Growth'].value_counts())