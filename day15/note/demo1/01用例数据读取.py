"""
============================
Author:柠檬班-木森
Time:2020/2/7   20:17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import openpyxl

# 打开文件，加载到工作簿对象
wb = openpyxl.load_workbook("cases.xlsx")

# 选择表单
sh = wb["login"]

# 需求：将注册的用例数据读取出来，每条用例保存为一个字典（表格中的标题作为键），所有的用例放到一个列表中

# 按行获取表单所有格子中的数据，每一行的数据放在一个元组中
datas = list(sh.rows)
# 获取第一行的数据，作为字典的键
title = [i.value for i in datas[0]]
# 创建一个空列表，用例存放用例数据
cases = []
# 遍历除第一行之外的数据
for i in datas[1:]:
    # 获取该行数据的值
    values = [c.value for c in i]
    # print(values)
    # 将该行数据和title（第一行数据）打包转换为字典
    case = dict(zip(title,values))
    # print(case)
    # 将转换的字典添加到前面创建的空列表cases中
    cases.append(case)

print(cases)


# # 获取第二行的数据
# li2 = [i.value for i in datas[1]]
#
# # 通过zip打包转换为字典
# data = dict(zip(li1, li2))
# print("读取出来保存的数据：",data)










