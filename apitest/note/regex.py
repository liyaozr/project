"""
============================
Author:luli
time:2020/2/27
company:happy
============================
"""
import re

'''
1、写一个正则表达式，能匹配所有合法的python标识符
只能由数字、字母、下划线组成，并且不能用数字开头
不能用python中的关键字,不能一模一样
'False', 'None', 'True', 'and', 'as', 'assert', 'async',
'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
'else', 'except', 'finally', 'for', 'from', 'global', 'if',
'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
'raise', 'return', 'try', 'while', 'with', 'yield'

2、s="1987-02-09 07:30:00 "，匹配出前面字符串中的年 月 日

3、s="aaaa  xiasd@163.com 77777777777 xiaori@139.com aaaaaaa"",匹配前面字符串中的所有的邮箱地址
'''
str1 = '''find_num  7val  add. def  
        pan -print  open_file  FileName 
        9prints INPUT  ls  user^name  
        list1  str__888  is  true none try'''

# res1 = re.findall(
#     r'(?!def|False|None|True|and|as|assert|async|await|break|class|continue|is|del|elif|else|except|finally|for|from|global|if|import|in|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)[a-zA-Z_]\w*',
#     str1)
# print(res1)

str2 = "1987-02-09 07:30:00"
res2 = re.findall(r'\d{4}-\d{2}-\d{2}', str2)
# print(res2)


str3 = "aaaa  xiasd@163.com 77777777777 xiaori@139.com aaaaaaa"
res3 = re.findall(r'\w*@\d{3}.com', str3)
# print(res3)
