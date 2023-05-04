import pandas as pd
import glob
import numpy as np
#from operator import operator

data_files = glob.glob("filename*.csv")
# print(data_files)

list_df =[]
for csvfiles in data_files:
    df = pd.read_csv(csvfiles, header=None)
    list_df.append(df)
# print(list_df)


merged_data = pd.concat(list_df)
# print(merged_data)
merged_data.to_csv("combined.csv")


df = pd.read_csv("combined.csv", header=None)
df_2 = df.dropna()
# print(df_2)
col_1 = df_2[8].array
col_2 = df_2[9].array
col_0 = df_2[5].array
print(col_1)
col_1 = np.divide(col_1,100)
print(col_1)
key = 0
for value in col_2:
    cellItem = col_2[key]
    # print('123' + cellItem + '123')
    if cellItem == ' ':
        col_2[key] = 1
    else:
        col_2[key] = -1
    key = key + 1

# print(col_1)
# print(col_2)

r1 = np.multiply(col_1,col_2).sum()
#print((col_0[0]))
print(f"File Name: {col_0[0]}, Output value: {r1}")