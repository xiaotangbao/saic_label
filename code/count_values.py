# coding=utf-8
import pandas as pd

#导入数据
filename = "F:\Maicmotor\intern\saic_label\labeled_data_first\labeled_data_utf8\output\\auto_home_20171106_3k_revised.csv"
data = pd.read_csv(filename)

#统计sentiment_label
print(data['auto_related'].value_counts())
print(data['sentiment_label'].value_counts())