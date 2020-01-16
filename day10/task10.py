"""
============================
Author:luli
Time:2020/1/16
Company:Happy
============================
"""
import os
import random

'''
1、实现一个文件复制器函数，通过给函数传入一个路径，复制该路径下面所有的文件(目录不用复制)到当前目录，
要求：如果传路径不存在，不能报错                
提示：os模块结合文件读写操作 、异常捕获 即可实现
'''


def file_copy(file_path):
    print(file_path)
    # 如果给的路径是文件路径，读取它的目录
    if os.path.isfile(file_path):
        file_path = os.path.dirname(file_path)
    try:
        dir_list = os.listdir(file_path)
        print(dir_list)
    except:
        print('目录路径有误或者不存在')
    else:
        new_dir = os.path.dirname(__file__)
        for item in dir_list:
            item_dir = os.path.join(file_path + '/' + item)
            # 判断item是不是文件
            if os.path.isfile(item_dir):
                with open(item_dir, 'r', encoding='utf8') as f1:
                    content = f1.read()
                    new_item_dir = os.path.join(new_dir + '/' + item)
                    with open(new_item_dir, 'w', encoding='utf8') as f2:
                        f2.write(content)
            else:
                # 本来想创建文件夹，然后再复制，没想好怎么写
                file_copy(item_dir)


# 如果输入的路径是文件名
# file_copy(r'E:\project\day5\01集合的定义.py')
# 如果输入的路径是目录
# file_copy(r'E:\project\day1')


'''
2、改善上节课扩展作业的注册程序，打开文件的读取数据的时候，如果文件不存在会报错，请通过try-except来捕获这个错误，进行处理，让注册程序可以继续运行。
'''


# 密码确认
def pwd_confirm(user, user_list):
    while True:
        pwd1 = input('请输入密码：')
        pwd2 = input('请再次输入密码：')
        if pwd1 == pwd2:
            user_list.append({'user': user, 'pwd': pwd1})
            print('注册成功')
            break
        else:
            print('两次输入的密码不一致，请重新输入')


def register():
    try:
        # 文件存在走这里
        with open('user_list.txt', 'r+', encoding='utf8') as f3:
            user_list = eval(f3.read())
    except:
        # 文件不存在走这里
        with open('user_list.txt', 'w+', encoding='utf8') as f3:
            user_list = []
            user = input('请输入用户名：')
            pwd_confirm(user, user_list)
            user_list = str(user_list)
            f3.write(user_list)
    else:
        while True:
            user = input('请输入用户名：')
            for item in user_list:
                if user == item['user']:
                    print('该用户名已被注册，请重新输入')
                    break
            else:
                pwd_confirm(user, user_list)
                break
        user_list = str(user_list)
        with open('user_list.txt', 'w', encoding='utf8') as f3:
            f3.write(user_list)


register()

'''
3、优化之前作业的石头剪刀布游戏，用户输入时，如果输入非数字会引发异常，请通过异常捕获来处理这个问题。
'''
# while True:
#     try:
#         input_num = int(input('请输入出拳数字：石头（1）／剪刀（2）／布（3）/退出（4）'))
#     except:
#         print('您输入的不是数字，请重新输入')
#     else:
#         random_num = random.randint(1, 3)
#         print(random_num)
#         if input_num > 4 or input_num < 1:
#             print('你输入的数字有误')
#         elif input_num == 4:
#             exit('-----您选择退出游戏------')
#         elif input_num - random_num == -1 or input_num - random_num == 2:
#             print('你赢了')
#         elif input_num - random_num == -2 or input_num - random_num == 1:
#             print('你输了')
#         else:
#             print('平局')
