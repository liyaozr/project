"""
============================
Author:柠檬班-木森
Time:2020/1/13   21:12
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
文件读取的方法
read:读取文件中所有的内容，该方法可以通过参数去指定读取内容的大小
readline:每次读取一行内容
readlines:按行读取所有的内容，每一行作为一个元素，放到一个列表中



"""

# # 读取不在同一个目录下的文件，要写上文件的完整路径
f = open("tttt.txt", "r", encoding="utf8")

# 按行读取内容：每次读取一行
# content = f.readline()
# print(content)
#
# content1 = f.readline()
# print(content1)
#
# content2 = f.readline()
# print(content2)

# 按行读取所有的内容，每一行作为一个元素，放到一个列表中

datas = f.readlines()
print(datas)
#
# # 关闭文件
f.close()
