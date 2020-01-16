"""
============================
Author:柠檬班-木森
Time:2020/1/15   20:44
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
os模块：python内置的模块之一，它的作用时用来和操作系统进行交互的

os模块中需要掌握的内容：处理路径

os.path.dirname:获取 给定文件路径 所在的目录路径（获取父级目录）

os.path.join:用来进行路径拼接的模块

os.path.abspath:获取绝对路径


window系统中的路径使用的是\

linux系统中的路径使用的是/


"""
import os
# 获取当前文件的路径
path = __file__
print("当前文件的路径：", path)
# 获取当前文件所在的目录路径
d1_path = os.path.dirname(path)
print(d1_path)
# print(d1_path+"/cases.txt")
file_path = os.path.join(d1_path,"cases.txt")
# os模块拼接出来的路径如果出现/和\都有的情况（不用管，可以使用的）
print(file_path)







with open(file_path, "r", encoding="utf8")as f:
    content = f.read()
    print(content)


# with open(r"C:\project\py26_project\py26_10day\cases.txt", "r", encoding="utf8")as f:
#     content = f.read()