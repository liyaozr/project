"""
============================
Author:柠檬班-木森
Time:2020/1/17   20:19
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
异常捕获时：语法错误是捕获不到的

在except 后面可以指定捕获的异常类型
except NameError
如果要捕获多个异常类型：

方式一：使用多个except,每个except都可以指定捕获的异常类型，适合不同类型的异常做不同的处理

方式二：使用一个except捕获多个类型的异常，适用捕获到的多个类型的异常类型，采用相同的处理方式


方式三：捕获所有的异常类型（语法错误除外）

"""
# f = open("ttt.txt", 'r', encoding="utf8")
# print(a)
print('------------开始执行-------------------')

# 使用多个except,每个except都可以指定捕获的异常类型，适合不同类型的异常做不同的处理
# try:
#     print(110)
#     print(a)
#     f = open("ttt.txt", 'r', encoding="utf8")
# except NameError as e:
#     print("代码有异常")
#     print('异常信息：',e)
# except FileNotFoundError as e:
#     print("代码发生了异常")
#     print('异常信息：', e)
# else:
#     print("代码没有异常")
# finally:
#     print("代码不管有没有异常都会执行")

# 使用一个except捕获多个类型的异常，适用捕获到的多个类型的异常类型，采用相同的处理方式

# try:
#     print(110)
#     print(a)
#     f = open("ttt.txt", 'r', encoding="utf8")
# except (NameError, FileNotFoundError, KeyError, ValueError) as e:
#     print("代码有异常")
#     print('异常信息：', e)
# else:
#     print("代码没有异常")
# finally:
#     print("代码不管有没有异常都会执行")

# try:
#     print(a)
# except:
#     print("捕获到了异常")

# 捕获所有的异常类型（语法错误除外）,像一些第三方模块中自定义的异常，就可以使用该方式来进行捕获
# try:
#     # print(a)
#     f = open("ttt.txt", 'r', encoding="utf8")
# except Exception as e:
#     print("捕获到了异常")
