"""
============================
Author:柠檬班-木森
Time:2020/1/20   21:44
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
继承的类不在同一个模块：先导入再继承



多继承：一个类可以同时继承多个父类,他会将所有父类的方法都继承过来







"""


# ---------------------继承的类不在同一个模块-------------------
# from py26_12day.phone import BasePhone
#
#
# class PhoneV1(BasePhone):
#     def func(self):
#         print("这个是func方法")
#
# p1 = PhoneV1()
# p1.tell()
# -------------------多继承-------------------------
#
#
# class Base(object):
#     def func(self):
#         print("----base----func-----")
#
#     def fun(self):
#         print("----base----fun----")
#
#
# class A(object):
#     def func_a(self):
#         print("----A----func-----")
#
#     def fun(self):
#         print("----A----fun----")
#
#
# class B(object):
#     def func_b(self):
#         print("----B----func-----")
#
#     def fun(self):
#         print("----B----fun----")
#
#
# class MyClass(Base, A, B):
#     def func_my(self):
#         print("----func_my----func-----")
#
#     # def fun(self):
#     #     print("----func_my----fun----")
#
#
# m = MyClass()
#
# # m.func_my()
# # m.func()
# # m.func_a()
# # m.func_b()
#
#
# m.fun()


class Base(object):
    def fun(self):
        print("----base----fun----")


class A(Base):
    def fun(self):
        print("----A----fun----")


class B(object):
    def fun(self):
        print("----B----fun----")


class MyClass(A, B):
    def func_my(self):
        print("----func_my----func-----")


m = MyClass()

m.fun()
