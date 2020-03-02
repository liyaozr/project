"""
============================
Author:柠檬班-木森
Time:2020/1/13   20:10
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
filter:过滤器
第一个参数：函数
第二个参数：可迭代对象
过滤的原理:filter会将第二个参数中的数据，进行遍历，然后当成参数传入第一个参数（函数中），根据
         函数返回的结果是否为True，来决定是否要将改数据过滤出来


iterable:可迭代对象
可以使用for循环进行遍历的都是可迭代对象。
已学过的数据类型（属于可迭代对象的）：字符串，列表，元组，字典，集合、range创建的数据


"""


# filter 运行的原理
# def func(a):
#     print("这个是函数func")
#     print("这个是传入的参数a：", a)
#
#
# li = [11, 22, 33, 44, 111, 222, 222]
#
# res = filter(func, li)
#
# print(list(res))


def func(a):
    return a < 50


li = [11, 22, 33, 44, 111, 222, 222]

res = filter(func, li)
print(res)

print(set(res))
