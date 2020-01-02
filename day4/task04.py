"""
============================
Author:luli
Time:2019/12/31
Company:Happy
============================
"""

'''
一、现在有一个列表 li2=[1，2，3，4，5]，
     第一步：请通过三行代码将上面的列表，改成这个样子 li2 = [0，1，2，3，66，5，11，22，33]
     第二步：对列表进行升序排序 （从小到大）
     第三步：将列表复制一份进行降序排序（从大到小）
'''
# 第一步
# li2 = [1, 2, 3, 4, 5]


# li2.insert(0, 0)
# li2[4] = 66
# li2.extend([11, 22, 33])

# print(li2)

# 第二步
# li2.sort()
# print(li2)
#
# 第三步
# li3 = li2.copy()
# 方法1
# li3.reverse()
# print(li3)
# 方法2
# print(li3[::-1])

'''
二、定义一个空列表user=[],   分别提示用户输入，姓名，年龄，身高，用户输入完之后，
将输入的信息作为添加的列表中保存，然后按照一下格式输出：
用户的姓名为：xxx,年龄为：xxx,  身高为：xxx  ,请仔细核对（要求：输出的身高要求保留2位小数）
'''
# user = []
# name = input('请输入您的姓名：')
# age = int(input('请输入您的年龄：'))
# height = round(float(input('请输入您的身高：')), 2)
#
# user = [{'name': name}, {'age': age}, {'height': height}]
#
# print(user)
# print(f'用户的姓名为：{name}，年龄为{age}，身高为：{height}，请仔细核对')

'''
三、有下面几个数据 ，
t1 = ("aa",11)      t2= (''bb'',22)    li1 = [("cc",11)]
请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":22,"bb":22}
要注意字典中元素的顺序（使用python3.5以下的同学不用考虑位置）
'''

# t1 = ("aa", 11)
# t2 = ("bb", 22)
# li1 = [("cc", 11)]
#
# li1.insert(0, t1)
# li1.insert(2, t2)
# print(li1)
#
# dic1 = dict(li1)
# dic1['cc'] = 22
# print(dic1)

'''
四、有5道题（通过字典来存储数据）： 某比赛需要获取你的个人信息，设计一个程序， 
 1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据存储起来，
 2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
 3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 
 4、平台为了保护你的隐私，需要你删除你的联系方式；
 5、你为了取得更好的成绩， 你添加了一项自己的擅长技能。
'''
# # 1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据存储起来
# user_info = {'name': input('请输入您的姓名：'), 'age': int(input('请输入您的年龄：')), 'sex': input('请输入您的性别：')}
#
# # 2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
# # 方法1
# print(f'我的名字{user_info["name"]}，今年{user_info["age"]}岁，性别{user_info["sex"]}，喜欢敲代码')
#
# # 方法2
# print('我的名字{}，今年{}岁，性别{}，喜欢敲代码'.format(user_info["name"], user_info["age"], user_info["sex"]))
#
# # 3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式
# # 方法1
# user_info['height'] = input('请输入您的身高：')
# user_info['tel'] = input('请输入您的联系方式：')
# print(user_info)
# # 方法2
# user_info.update({'height': float(input('请输入您的身高：')), 'tel': input('请输入您的联系方式：')})
# print(user_info)
#
# # 4、平台为了保护你的隐私，需要你删除你的联系方式；
# user_info.pop('tel')
# print(user_info)
#
# # 5、你为了取得更好的成绩， 你添加了一项自己的擅长技能。
# user_info['skill'] = 'sing'
# print(user_info)

'''
五、请指出下面那些为可变类型的数据，那些为不可变类型的数据
1、 (11)           数值，不可变
2、 "111"          字符串，不可变
3、 ([11,22,33])   列表，可变
4、 {"aa":111}     字典，可变
'''
# print(type((11)))  # <class 'int'>
# print(type("111"))  # <class 'str'>
# print(type(([11, 22, 33])))  # <class 'list'>
# print(type({"aa": 111}))  # <class 'dict'>

'''
6、请获取下面数据中的token，和reg_name
'''
data = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 74711,
        "leave_amount": 29600.0,
        "mobile_phone": "13367899876",
        "reg_name": "小柠檬666",
        "reg_time": "2019-12-13 11:12:53.0",
        "type": 0,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2019-12-30 22:28:57",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjc0NzExLCJleHAiOjE1Nzc3MTYxMzd9.eNMtnEWr57iJoZRf2IRsGDWm2GKj9LZc1J2SGRprAwOk7EPoJeXSjJwdh0pcVVJygHmsbh1TashWqFv1bvCVZQ"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved"
}
# print(data['data']['token_info']['token'])
# print(data['data']['reg_name'])

'''
7、切片 
 1、li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9] 
 2、s = 'python java php',通过切片获取: java
 3 、tu = ('a','b','c','d','e','f','g','h'),通过切片获取 ['g','b']
'''
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(li[2::3])
# print(li[-7::3])
#
# s = 'python java php'
# print(s[7:11])
# print(s[-8:-4])
# print(s[7:-4])
# print(s[-8:11])
#
# tu = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
# print(tu[-2::-5])
# print(tu[6::-5])


'''
8、请分别列出学过的字符串方法，列表的方法、字典的方法、元祖的方法，并指出方法的作用

字符串方法:
1、字符串拼接：
join():拼接字符串，相当于粘合剂   eg:join(s1,s2,s3),拼接字符串s1,s2,s3
format():格式化输出    eg：print('明天周{}，去{}城市'.format(参数1，参数2))
2、查询
index():根据下标查询元组列表字符串的值
find():把参数作为子串，在规定的始末位置进行查找   eg:  find(bug,start=0,end=len(str))
count()：记录字符串中某个元素出现的次数
3、分割
split():根据参数分割字符串   eg:split(','),按照逗号分割字符串
4、替换
replace():根据参数替换字符串   eg：replace(想替换的老值，要换的的新值，替换多少次)
5、大小写转换
upper():将字符串全部转化为大写
lower():将字符串全部转换为小写

列表方法：
1、添加
append():在列表末尾新增一个值
insert():在指定位置插入元素，有两个参数，第一个参数表示插入的位置，第二个才是要插入的数据
extend():在列表末尾加上一个或多个元素
2、删除
remove():删除指定的元素，（）中应该是要删除的元素，而不是下标
pop():根据下标删除对应的元素，不传参数默认删除最后一个
clear():清空列表
3、查询
index():根据下标查询元组列表字符串的值
count():查询某个元素在列表中出现的次数
4、排序
sort():对列表进行排序，无参数时默认从小到大排序，需要从大到小排序时sort(reverse=True)
5、复制
copy():对列表进行复制
6、反转
reverse():将列表的顺序反转



字典的方法：
1、添加/修改
update():一次往字典中添加多个键值对，存在则是修改
2、删除
pop():删除字典给定键 key 及对应的值，返回值为被删除的值。key 值必须给出。 否则，返回默认值
popitem():随机返回并删除字典中的最后一对键和值
3、查询
get():返回指定键的值，如果值不在字典中返回默认值
4、复制
copy():对字典的所有键值对进行复制
5、其他方法
values():返回字典所有值
keys():返回字典中所有的键
items():返回字典中所有的键值对

clear():清空字典



元组的方法：
index():根据下标查询元组列表字符串的值
count():查询某个元素在元组中出现的次数

'''
