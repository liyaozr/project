# 第一题
def work1():
    # 第一步：读取数据,每一行作为一个元素放到列表中
    with open('data.txt', encoding='utf8') as f:
        datas = f.readlines()
        print(datas)
    # 第二步：将数据转换为字典
    # 创建一个空字典
    dic = {}
    # 通过enumerate去获取列表中的数据和下标
    for index, data in enumerate(datas):
        # 构造数据的key和value
        key = 'data{}'.format(index)
        value = data.replace('\n', '')
        # 加入到字典中
        dic[key] = value



    return dic


res = work1()
print('第一题最终的数据为：', res)


# 第二题
# 要求一：
def work2_1():
    # 第一步：读取数据,每一行作为一个元素放到列表中
    with open('cases.txt', 'r') as f:
        datas = f.readlines()
    # 第二步：将数据转换为列表
    # 创建一个空列表
    cases = []
    # 遍历出来每一行数据
    for i in datas:
        # 将该行数据使用split按，进行分割,得到一个列表
        itme = i.split(',')
        # 创建一个空字典，用例存放该行数据
        dic = {}
        # 遍历分割后的列表，
        for j in itme:
            # 将遍历出来的数据，按:分割，得到key,value,然后加入到字典中
            key = j.split(':')[0]
            value = j.split(':')[1].replace('\n', '')
            dic[key] = value
        # 将该行数据加入到列表中
        cases.append(dic)
    # 完成转换之后，将转换后的数据 进行返回
    return cases


data2 = work2_1()
print('第二题最终的数据为：', data2)

#  扩展题：不要求提交
"""
注意点：
我这边数据存储的格式为[{},{}...] ，需要先创建一个users.txt文件并写入一个空列表：[]，
如果没有创建users.txt文件会报错，请先创建一个users.txt文件，写入以下内容
数据为一个空列表，下如：
[]
"""


def work3():
    # 读取文件中注册用户的数据
    with open('users.txt', 'r', encoding='utf8') as f:
        # 读取内容,使用eval识别字符串中的列表
        users = eval(f.read())

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
        # 将列表转换为字符串,写入文件
        f.write(str(users))


work3()
