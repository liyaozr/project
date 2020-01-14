"""
============================
Author:luli
Time:2020/1/14
Company:Happy
============================
"""

'''
第一题：当前有一个txt文件，内容如下：
数据aaa
数据bbb
数据ccc
数据ddd
# 要求：请将数据读取出来，保存为以下格式
{'data0': '数据aaa', 'data1': '数据bbb', 'data2': '数据ccc', 'data3': '数据ddd'}
​
# 提示：
# 可能会用到内置函数enumerate
​
# 注意点：读取出来的数据如果有换行符'\n'，要想办法去掉。
'''


def task1():
    with open('task09.txt', 'r', encoding='utf8') as f1:
        content = f1.readlines()
        content = [item.replace('\n', '') for item in content]
        print(content)  # ['数据aaa', '数据bbb', '数据ccc', '数据ddd']
        res = enumerate(content)
        content_dict = {'data{}'.format(key[0]): key[1] for key in res}
        print(content_dict)  # {'data0': '数据aaa', 'data1': '数据bbb', 'data2': '数据ccc', 'data3': '数据ddd'}


# task1()

'''
第二题：当前有一个case.txt文件，里面中存储了很多用例数据: 如下，每一行数据就是一条用例数据，
url:www.baidu.com,mobilephone:13760246701,pwd:123456
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
# 要求一： 请把这些数据读取出来，到并且存到list中，格式如下
[
{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'}, {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}
]
​
# 提示：可以分析读取出来的每一行字符串中的内容，然后使用的字符串分割方法进行分割，想办法组装成字典。
# 注意点：数据中如果有换行符'\n'，要想办法去掉。
'''


def task2():
    with open('case.txt', 'r', encoding='utf8') as f2:
        content = f2.readlines()
        # 去掉换行符+分割
        content = [item.replace('\n', '').split(',') for item in content]
        # 组成字典
        content = [{key for key in item} for item in content]
        print(content)


# task2()

# 打印结果
'''
[
{'url:www.baidu.com', 'mobilephone:13760246701', 'pwd:123456'}, 
{'url:www.baidu.com', 'mobilephone:15678934551', 'pwd:234555'}, 
{'url:www.baidu.com', 'mobilephone:15678934551', 'pwd:234555'}, 
{'url:www.baidu.com', 'mobilephone:15678934551', 'pwd:234555'}, 
{'url:www.baidu.com', 'mobilephone:15678934551', 'pwd:234555'}
]
'''

'''
第四题：扩展题（不要求提交，有时间的同学可以去思考一下）：
之前作业写了一个注册的功能，再之前的功能上进行升级，
要求：把所有注册成功的用户数据放到文件中进行保存，确保下一次运行代码的时候，上一次运行注册的账号数据还在。
'''


def register():
    with open('user_list.txt', 'a+', encoding='utf8') as f3:
        user_list = f3.readlines()
        print(user_list)
    # while True:
    #     user = input('请输入用户名：')
    #     for item in user_list:
    #         if user == item['user']:
    #             print('该用户名已被注册，请重新输入')
    #             break
    #     else:
    #         while True:
    #             pwd1 = input('请输入密码')
    #             pwd2 = input('请再次输入密码')
    #             if pwd1 == pwd2:
    #                 user_list.append({'user': user, 'pwd': pwd1})
    #                 print('注册成功')
    #                 break
    #             else:
    #                 print('两次输入的密码不一致，请重新输入')
    #         break
    # print(user_list)


register()
