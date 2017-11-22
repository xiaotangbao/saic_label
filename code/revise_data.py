# coding=utf-8
import pandas as pd

#revise数据,修改错误格式
filename = "F:\Maicmotor\intern\saic_label\labeled_data_utf8\\output\\auto_home_20171106_3k.csv"
data = pd.read_csv(filename)
data_auto_senti_before = data.drop_duplicates(['sentiment_label','auto_related'])[['auto_related','sentiment_label']]
data.replace('np', 'ns',inplace=True)
data['auto_related'][(data['auto_related'] == 0) & (data['sentiment_label'] == '-1')] = 1
data['sentiment_label'][data['sentiment_label'] == '0-1'] = 'ns'
data['sentiment_label'][(data['auto_related'] == 1) & (data['sentiment_label'].isnull())] = 'ns'
data['sentiment_label'][(data['auto_related'].isnull()) & (data['sentiment_label'].isnull())] = 'ns'
data['sentiment_label'][(data['auto_related'] == 0) & (data['sentiment_label'] == '1')] = '0'
data['auto_related'].fillna(1,inplace=True)
data.replace(0,'0',inplace=True)
data.replace(1,'1',inplace=True)
data.replace('-','ns',inplace=True)
data['sentiment_label'].fillna('0',inplace=True)
data_auto_senti_after = data.drop_duplicates(['sentiment_label','auto_related'])[['auto_related','sentiment_label']]
data_saic = data

# 输出修正后的数据（3k）
filename = "F:\Maicmotor\intern\saic_label\labeled_data_first\labeled_data_utf8\output\\auto_home_20171106_3k_revised.csv"
data_saic.to_csv(filename,encoding='utf-8',index=False)