"""
============================
Author:柠檬班-木森
Time:2020/1/15   21:20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import os

# 获取当前工作路径等同于linux下的pwd
# p1 = os.getcwd()
# print(p1)

# 切换路径：cd
# os.chdir("../../..")
# print(os.getcwd())

# 创建文件夹：mkdir
# os.mkdir("pake02")

# 删除文件夹:rmdir
# os.rmdir("pake02")


# 获取当前目录下的文件及文件夹信息：listdir
# （默认获取的是当前工作目录）可以接收一个参数:用来指定获取的路径
# print(os.listdir(r"C:\project\py26_project"))

# 判断给定的路径是否是文件(如果是则返回True,否则返回false)
# res = os.path.isfile(r"C:\project\py26_project\py26_10day")
# print(res)
# 判断给定的路径是否是目录（文件夹）:如果是则返回True,否则返回false)
# res = os.path.isdir(r"C:\project\py26_project\py26_10day\data.txt")
# print(res)