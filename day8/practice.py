"""
============================
Author:luli
time:2020/1/10
company:happy
============================
"""

import keyword

print(keyword.kwlist)


# def fun1(a=100, b):
#     print('hello')
#     print(a + b)
#
#
# print(fun1(100))


# def func(a, b, *args):
#     print(args)
#     return a + b
#
#
# res = func(11, 22, 111, 222)
# print('相加的结果为：', res)


def func(a, b, **kwargs):
    print(**kwargs)
    return a + b


res = func(11, 22, c=111, d=222)

# li = [1, 2, 3]
# tu = (11, 22, 33)
# dic = {'a': 111, 'b': 222, 'c': 333}
#
#
# def func(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
#
# func(*li)
# func(*tu)
# func(**dic)
