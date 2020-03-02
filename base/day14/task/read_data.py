"""
============================
Author:luli
time:2020/1/24
company:happy
============================
"""

import openpyxl

'''
通过代码读取附件文件中的register这个表单的第一行和第二行数据，想办法保存为一个字典：格式如下：

{'case_id': 1, 'title': '正常注册', 'data': "('python1', '123456', '123456')", 'expected': '{"code": 1, "msg": "注册成功"}', 'result': None}
'''

wb = openpyxl.load_workbook('cases.xlsx')
sh = wb['register']
datas = list(sh.rows)
title = ['case_id', 'title', 'data', 'expected', 'result']

li1 = [i.value for i in datas[1]]
li2 = [i.value for i in datas[2]]

dict1 = dict(zip(title, li1))
dict2 = dict(zip(title, li2))

print(dict1)
print(dict2)
