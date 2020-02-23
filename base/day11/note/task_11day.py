"""
============================
Author:柠檬班-木森
Time:2020/1/16   22:38
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import random
import os


def copy_file(path):
    # 第一步：获取目标路径中所有的文件和目录
    try:
        file_list = os.listdir(path)
    except:
        print('传入的路径不正确')
    else:
        # 第二步：遍历文件，
        for item in file_list:
            # 获取该文件的路径
            file_path = os.path.join(path, item)
            # 第三步：判断是文件还是目录，是文件的话就进行copy
            if os.path.isfile(file_path):
                # 打开文件，读取内容
                with open(file_path, 'r', encoding='utf8') as f:
                    contnet = f.read()

                # 在当前目录创建副本文件，写入内容
                new_file = 'cp' + item
                with open(new_file, 'w', encoding='utf8') as f:
                    f.write(contnet)


copy_file(r'C:\project\py26_project\py26_01day')



def work2():
    try:
        # 读取文件中注册用户的数据
        with open('users.txt', 'r', encoding='utf8') as f:
            # 读取内容
            data = f.read()
            # 识别字符串中的列表
            users = eval(data)
    except:
        # 文件不存在，将users设置为一个空列表
        users = []

    # 注册功能代码（上次作业写的，不需要改动）
    username = input('请输入新账号:')  # 输入账号
    password1 = input('请输入密码：')  # 输入密码
    password2 = input('请再次确认密码：')  # 再次确认密码

    for user in users:  # 遍历出所有账号，判断账号是否存在
        if username == user['name']:
            print('该账户已存在')  # 账号存在，
            break
    else:
        # 判断两次密码是否一致
        if password1 != password2:
            print('注册失败，两次输入的密码不一致')
        else:
            # 账号不存在 密码一样，则添加到账户列表中
            users.append({'name': username, 'pwd': password2})
            print('注册成功！')

    # 程序运行结束后，将所有用户的数据写入文件
    with open('users.txt', 'w', encoding='utf8') as f:
        # 将列表转换为字符串
        content = str(users)
        # 写入文件
        f.write(content)


# work2()
# 第三题
def work3():
    print('---石头剪刀布游戏开始----')
    print('请按下面提示出拳：')
    # 创建一个列表来存储 石头 剪刀 布
    li = ['石头', '剪刀', '布']

    while True:
        print('石头【1】 剪刀【2】 布【3】 结束游戏【4】')
        # 用户输入数字
        try:
            user_num = int(input('请输入你的选项：'))
        except:
            print('您出拳有误，请按规矩出拳')
        else:
            # 电脑随机生成数字
            r_num = random.randint(1, 3)
            if 1 <= user_num <= 3:
                # 判断用户和电脑是否相等
                if r_num == user_num:
                    print('您的出拳为:{}，电脑出拳:{}，平局'.format(li[user_num - 1], li[r_num - 1]))
                # 判断用户胜利的情况
                elif (user_num - r_num) == -1 or (user_num - r_num) == 2:
                    print('您的出拳为:{}，电脑出拳:{}，您胜利了'.format(li[user_num - 1], li[r_num - 1]))
                else:
                    print('您的出拳为:{}，电脑出拳:{}，您输了'.format(li[user_num - 1], li[r_num - 1]))
            # 用户输入4，游戏结束
            elif user_num == 4:
                print('游戏结束')
                break
            else:
                print('您出拳有误，请按规矩出拳')

# work3()
