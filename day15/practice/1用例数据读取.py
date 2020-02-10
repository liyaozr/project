"""
============================
Author:luli
time:2020/1/24
company:happy
============================
"""

import openpyxl

# 1、打开工作簿
wb = openpyxl.load_workbook('cases.xlsx')

# 2、打开表单
sh = wb['login']

# 3、读取数据
datas = list(sh.rows)
# print(datas)
# 表头
title = [i.value for i in datas[0]]
# print(title)
# 内容
cases = []
for item in datas[1:]:
    values = [i.value for i in item]
    case = dict(zip(title, values))
    cases.append(case)

print(cases)
