# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 12:22:00 2018

@author: T
"""

import pandas as pd
import os


#file_path = r"E:\DataCastle\1.凤凰金融\round2\round2"
file_list = os.listdir(r"D:\DCmatch\fhfinance\round3")

data_list = []

#读入每天数据
for i in range(len(file_list)):
    datas = pd.read_csv("D:\\DCmatch\\fhfinance\\round3\\" + file_list[i])
    datas["days"] = int(file_list[i].split(".")[0])
    data_list.append(datas)

#获取表头
col_list = list(data_list[0].columns)

'''
#获取所有股票代码
code_list = []l
for i in range(len(data_list)):
    code_list = list(set(list(data_list[i].code) + code_ist))
'''
if __name__ == '__main__':

    df = pd.DataFrame()

    for j in range(len(data_list)):
        df = pd.concat((df,data_list[j]))

    df.to_csv("all_data.csv",index=False)