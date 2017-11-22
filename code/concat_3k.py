# coding=utf-8
import pandas as pd

# concat 3k
i = 1
filename = "F:\Maicmotor\intern\saic_label\labeled_data_utf8\\auto_home_20171106_" + str(i) + ".csv"
data = pd.read_csv(filename)
for i in range(2,19):
    filename = "F:\Maicmotor\intern\saic_label\labeled_data_utf8\\auto_home_20171106_" + str(i) + ".csv"
    data_add = pd.read_csv(filename)
    data = pd.concat([data,data_add])
    print(data.shape)

for i in range(22,34):
    filename = "F:\Maicmotor\intern\saic_label\labeled_data_utf8\\auto_home_20171106_" + str(i) + ".csv"
    data_add = pd.read_csv(filename)
    data = pd.concat([data,data_add])
    print(data.shape)

filename = "F:\Maicmotor\intern\saic_label\labeled_data_utf8\\output\\auto_home_20171106_3k.csv"
data.to_csv(filename,encoding='utf-8',index=False)