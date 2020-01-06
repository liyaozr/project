"""
============================
Author:柠檬班-木森
Time:2020/1/6   21:50
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
for循环的应用


遍历列表

遍历字符串

遍历字典

遍历元组

"""

# 遍历字符串
# s = "fghjkldd"
# for i in s:
#     print(i)

# 遍历元组
# tu = (11, 22, 3, 33, 4)
# for item in tu:
#     print(item)

# 遍历列表
# li = [11, 22, 33, 4, 5, 2, 5, 2]


# 字典的遍历
dic = {"name": "musne", "age": 18, "gender": "nan"}

# 直接遍历字典:遍历出来的是字典的键
# for i in dic:
#     print(i)


# 遍历字典中元素的值：values
# for i in dic.values():
#     print(i)


# 同时遍历字典的键和值：items
# 遍历出来的是一个包含键和值的元组
for i in dic.items():
    print(i)

# 使用两个变量对元组进行拆包
for k, v in dic.items():
    print("key:",k)
    print("value",v)
#     print("hello python")

# 元组拆包

# a = 100
# b = 200

# a, b = 100, 200
# print(a)
# print(b)

# 使用元组同时定义两个遍历，元组拆包
# c, d = (10, 20)
# print(c)
# print(d)


# tu = (11, 22, 333)
#
# aa, bb, cc = tu
# print(aa)
# print(bb)
# print(cc)
