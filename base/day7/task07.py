'''
============================
Author:luli
time:2020/1/8
company:happy
============================
'''

'''
1、一、输出99乘法表，结果如下：（提示嵌套for循环，格式化输出）
'''
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         # 1
#         print(f' {i} * {j} = {i * j}  ', end='')
#         # 2
#         # print(' {} * {} = {}  '.format(i, j, i * j), end='')
#     print(' ')

'''
2、有1 2 3 4 这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？
'''
# list_num = []
# for i in range(1, 5):
#     for j in range(1, 5):
#         for h in range(1, 5):
#             if i == j or i == h or j == h:
#                 continue
#             else:
#                 num = '{}{}{}'.format(i, j, h)
#                 list_num.append(num)
#
# print(list_num)
# print('一共有{}个互不相同且无重复数字的3位数'.format(len(list_num)))

'''
3、通过函数实现一个计算器，运行程序分别提示用户输入数字1，数字2，然后再提示用户选择 ：   
加【1】    减【2】    乘【3】      除【4】，根据不同的选择完成不同的计算 ，然后返回结果。
'''

# def calculator():
#     a = float(input('请输入数字1：'))
#     b = float(input('请输入数字2：'))
#     op = int(input('请选择运算方式：加【1】 减【2】 乘【3】 除【4】：'))
#     result = 0
#     if op == 1:
#         result = a + b
#     elif op == 2:
#         result = a - b
#     elif op == 3:
#         result = a * b
#     elif op == 4:
#         if b == 0:
#             return '0不能被整除'
#         else:
#             result = a / b
#     else:
#         return '您输入的运算符数字不规范'
#     return result
#
#
# print(calculator())

'''
4、实现一个注册的流程的函数，调用函数就执行下面要求功能
基本要求：
1、运行程序，提示用户，输入用户名，输入密码，再次确认密码。
2、判读用户名有没有被注册过，如果用户名被注册过了，那么打印结果该用户名已经被注册。
3、用户名没有被注册过，则判断两次输入的密码是否一致，一致的话则注册成功，否则给出对应的提示。
'''

def register():
    user_list = [{'user': 'liyaozhi', 'pwd': '123'}, {'user': 'lily', 'pwd': '1234'}, {'user': 'musen', 'pwd': '111'}]
    while True:
        user = input('请输入用户名：')
        for item in user_list:
            if user == item['user']:
                print('该用户名已被注册，请重新输入')
                break
        else:
            while True:
                pwd1 = input('请输入密码')
                pwd2 = input('请再次输入密码')
                if pwd1 == pwd2:
                    user_list.append({'user': user, 'pwd': pwd1})
                    print('注册成功')
                    break
                else:
                    print('两次输入的密码不一致，请重新输入')
            break
    print(user_list)


register()
