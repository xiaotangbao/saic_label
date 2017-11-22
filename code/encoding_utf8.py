# coding=utf-8
import pandas as pd
#转换编码格式，确保所有都是utf-8
def to_utf8(i):
    filename = "F:\Maicmotor\intern\saic_label\labeled_data\\auto_home_20171106_" + str(i) + ".csv"
    data = pd.read_csv(filename)
    filename = "F:\Maicmotor\intern\saic_label\labeled_data_utf8\\auto_home_20171106_" + str(i) + ".csv"
    data.to_csv(filename,index=False,encoding='utf-8')

for i in range(1,19):
    to_utf8(i)