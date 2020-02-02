"""
============================
Author:luli
time:2020/1/27
company:happy
============================
"""

# class TestClass:
#     attr = 100
#     _attr = 200
#     __attr = 300
#
#     def func1(self):
#         print('方法1')
#
#
# t1 = TestClass()

# print(t1.attr)  # 100
# print(t1._attr)  # 200
# print(t1.__attr)  # AttributeError: 'TestClass' object has no attribute '__attr'
# print(t1._TestClass__attr)


'''
------------------------实例方法、类方法、静态方法----------------------------
'''


class TestClass:

    def func1(self):
        print('方法1')

    @classmethod
    def func2(cls):
        print('方法2')


t1 = TestClass()
t1.func1()  # 方法1
# TestClass.func1()  # TypeError: func1() missing 1 required positional argument: 'self'

t1.func2()  # 方法2
TestClass.func2()  # 方法2
