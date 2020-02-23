"""
============================
Author:柠檬班-木森
Time:2020/2/6   10:13
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""

{'case_id': 1, 'title': '正常注册', 'data': "('python1', '123456', '123456')", 'expected': '{"code": 1, "msg": "注册成功"}', 'result': None}

"""


#  作业第三题：参考答案
import openpyxl

wb = openpyxl.load_workbook("cases.xlsx")

# 表单对象的rows属性
sh = wb["register"]

# 按行获取表单所有格子中的数据，每一行的数据放在一个元组中
datas = list(sh.rows)
# 获取第一行的数据
li1 = [i.value for i in datas[0]]
# 获取第二行的数据
li2 = [i.value for i in datas[1]]

print(li1)
print(li2)

# 通过zip打包转换为字典
data = dict(zip(li1, li2))
print("读取出来保存的数据：",data)
