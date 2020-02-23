'''
============================
Author:luli
time:2020/1/5
company:happy
============================
'''

import random

'''
一、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，
 要求一：去除列表中的重复元素，
 要求二：去重后删除 77，88，99这三个元素
'''
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]

# 去除列表中的重复元素
li = list(set(li))
print(li)
# 去重后删除 77，88，99这三个元素

# 方法1
# li.remove(77)
# li.remove(88)
# li.remove(99)
# print(li)

# 方法2
# li.sort()
# print(li[0:5])

'''
二、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给打九折， 
如果购买金额大于100元会给打八折。编写一程序，询问购买价格，再打印出折扣和最终价格。
'''

# total_price = float(input('请输入您的购买金额：'))
#
# if total_price > 100:
#     print('您的折扣为八折，最终价格为：', round(total_price * 0.8, 2))
# elif 50 <= total_price <= 100:
#     print('您的折扣为九折，最终价格为：', round(total_price * 0.9, 2))
# else:
#     print('您的购买金额未达到折扣标准，最终价格为：', round(total_price, 2))

'''
三、输入一个5位整数（不需要考虑其他数据类型），判断它个位与万位相同，十位与千位相同。 
根据判断打印出相关信息，相同打印结果：该数据符合规范，不相同打印：该数据不符合规范
'''

# num = input('请输入一个5位整数：')
# if len(num) != 5:
#     print('您输入的数字位数有误,请输入一个5位整数')
# else:
#     num_list = list(num)
#     if num_list[0] == num_list[4] and num_list[1] == num_list[3]:
#         print('该数据符合规范')
#     else:
#         print('该数据不符合规范')

'''
四、利用random函数生成随机整数（范围1-9），然后用户输入一个数字，来进行比较：
如果大于随机数，则打印印大于随机数。
如果小于随机数，则打印小于随机数。
如果相等随机数，则打印等于随机数。
'''
# random_num = random.randint(1, 9)
# print('随机数为：',random_num)
# input_num = float(input('请输入一个数字：'))
#
# if input_num > random_num:
#     print('大于随机数')
# elif input_num == random_num:
#     print('等于随机数')
# else:
#     print('小于随机数')

'''
五、实现剪刀石头布游戏，运行代码，提示用户输入出拳的数字 ：石头（1）／剪刀（2）／布（3）
电脑随机生成出拳数字，
然后比较胜负，打印游戏结果
'''
# input_num = int(input('请输入出拳数字：石头（1）／剪刀（2）／布（3）'))
# random_num = random.randint(1, 3)
# print(random_num)
#
# # 嵌套写
# if input_num == 1:
#     if random_num == 1:
#         print('平局')
#     elif random_num == 2:
#         print('你赢了')
#     else:
#         print('你输了')
# elif input_num == 2:
#     if random_num == 1:
#         print('你输了')
#     elif random_num == 2:
#         print('平局')
#     else:
#         print('你赢了')
# elif input_num == 3:
#     if random_num == 1:
#         print('你赢了')
#     elif random_num == 2:
#         print('你输了')
#     else:
#         print('平局')
# else:
#     print('你输入的数字有误')
#
# # 不嵌套
# if input_num == random_num:
#     print('平局')
# elif (input_num == 1 and random_num == 2) or (input_num == 2 and random_num == 3) or (
#         input_num == 3 and random_num == 1):
#     print('你赢了')
# elif (input_num == 1 and random_num == 3) or (input_num == 2 and random_num == 1) or (
#         input_num == 3 and random_num == 2):
#     print('你输了')
# else:
#     print('你输入的数字有误')
#
# # 简化判断
# if input_num > 3 or input_num < 1:
#     print('你输入的数字有误')
# elif input_num - random_num == -1 or input_num - random_num == 2:
#     print('你赢了')
# elif input_num - random_num == -2 or input_num - random_num == 1:
#     print('你输了')
# else:
#     print('平局')


''' 
六、提示用户输入一个数（只考虑整数），判断这个数能同时被3和5整除，
能整除打印 :这个数据我喜欢 
不能整除打印：这个数据不太喜欢
'''
# input_num = int(input('请输入一个整数：'))
# if input_num % 3 == 0 and input_num % 5 == 0:
#     print('这个数据我喜欢')
# else:
#     print('这个数据我不太喜欢')
