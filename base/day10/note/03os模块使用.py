"""
============================
Author:柠檬班-木森
Time:2020/1/15   21:04
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import os

# 如果在当前文件中获取项目路径

d1 = os.path.dirname(__file__)

print(d1)

d2 = os.path.dirname(d1)
print(d2)

base_dir = os.path.dirname(os.path.dirname(__file__))

print("项目目录的路径：", base_dir)

file_path = os.path.join(base_dir, "py26_01day/text.txt")
print(file_path)

#
# with open(file_path, "r", encoding="utf8")as f:
#     content = f.read()
#     print(content)


# ————————————————————————————————--os.path.abspath------------

# linux下的绝对路径表示
# print(__file__)

# 获取当前操作系统下的绝对路径表示方式
# print(os.path.abspath(__file__))


# 后面项目实战中获取项目绝对路径的方式
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
