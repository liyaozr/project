"""
============================
Author:luli
time:2020/1/10
company:happy
============================
"""

'''
# 第一题：现有数据如下
users_title = ["name", "age", "gender"]
users_info = [['小明', 18, '男'], ["小李", 19, '男'], ["小美", 17, '女']]

# 要求：将上述数据转换为以下格式
users = [{'name': '小明', 'age': 18, 'gender': '男'},
         {'name': '小李', 'age': 19, 'gender': '男'},
         {'name': '小美', 'age': 17, 'gender': '女'}]
'''
users_title = ["name", "age", "gender"]
users_info = [['小明', 18, '男'], ["小李", 19, '男'], ["小美", 17, '女']]

# 方法1
# def change():
#     users = []
#     for item in users_info:
#         user = dict(zip(users_title, item))
#         users.append(user)
#     return users
#
#
# print(change())

# 方法2
# users = [dict(zip(users_title, item)) for item in users_info]
# print(users)

'''
第二题：请封装一个函数，按要求实现数据的格式转换
# 传入参数： data = ["{'a':11,'b':2}", "[11,22,33,44]"]
# 返回结果：res = [{'a': 11, 'b': 2}, [11, 22, 33, 44]]
# 通过代码将传入参数转换为返回结果所需数据，然后返回
'''

# 方法1
# def format_conversion(data):
#     if type(data) == str:
#         res = eval(data)
#     else:
#         res = []
#         for item in data:
#             item = eval(item)
#             res.append(item)
#     return res


# 方法2
# def format_conversion(data):
#     if type(data) == str:
#         res = eval(data)
#     else:
#         res = [eval(item) for item in data]
#     return res


# print(format_conversion(["{'a':11,'b':2}", "[11,22,33,44]"]))
'''
第三题：简单题
#  1、什么是全局变量？
#  2、什么是局部变量？
#  3、函数内部如何修改全局变量（声明全局变量 ）？
#  4、写出已经学过的所有python关键字，分别写出用途？
'''
'''
1、全局变量：直接定义在模块中的变量，在该模块中任何地方都可以直接访问（使用）

2、局部变量：定义在函数内部的变量，只能在定义的那个函数内部使用

注意：尽量不要在函数内部定义和全局变量同名的变量，如果必须要定义一个同名的变量，建议放在函数的最前面

3、使用global声明某个变量之后，那么这个变量在函数内进行的操作会对全局生效

4、所有关键字
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 
'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 
'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

布尔值：False True
空；None
与、或、非：and or not
跳出循环：break continue
定义函数 def
删除：del 
控制流程：if  elif   else
循环：for while
引入：import  from
局部定义全局变量：global
包含：in
是否相等：is
空语句：pass
返回：return
'''
