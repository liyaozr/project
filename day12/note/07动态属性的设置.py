"""
============================
Author:柠檬班-木森
Time:2020/1/20   21:44
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
动态属性的设置：

内置函数setattr:设置属性
参数一：类名/对象
参数二：属性名
参数三：属性值


内置函数getattr:获取属性
参数一：类名/对象
参数二：属性名

内置函数delattr:删除属性
参数一：类名/对象
参数二：属性名

"""


class MyClass(object):
    ttt = 1000

    def __init__(self, gender):
        self.gender = gender


m = MyClass("女")

# ------------------------setattr----------------------
# 在类外面设置类属性
# 方式一
MyClass.attr = 100
# # 方式二：
# setattr(MyClass,"attr1",2000)
print(m.attr1)


# 在类外面给对象设置属性
# 方式一
# m.name = "小明"
# # 方式二：
# setattr(m, "age", 18)
#
# print(m.name)
# print(m.age)

# -------------------getattr--------------------
# 在类外面获取类属性
# 方式一
# print(MyClass.ttt)
# # 方式二
# print(getattr(MyClass, "ttt"))

# 在类外面获取对象属性
# 方式一
# print(m.gender)
# # 方式二
# print(getattr(m, "gender"))


# --------------------delattr---------------
# 在类外面删除类属性
# 方法一
# del MyClass.ttt

# 方式二
# delattr(MyClass,"ttt")
# print(MyClass.ttt)


# 在类外面删除对象属性
# 方法一
del m.gender

# 方式二
# delattr(m, "gender")


print(m.gender)
