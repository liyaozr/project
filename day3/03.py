'''
============================
Author:luli
time:2019/12/29
company:happy
============================
'''

import random


def is_num(input_info):
    try:
        float(input_info)
    except ValueError:
        return False
    else:
        return True


'''
1、用户输入一个数值，请使用比较运算符确认用户输入的是否为偶数？是偶数输出True,不是输出False（提示:input输入的不管是什么，都会被转换成字符串，自己扩展，想办法将字符串转换为数值类型，再做判段）
'''
# str1 = input('请输入数字：')

# 1
# if is_num(str1):
#     print(bool(float(str1) % 2 == 0))
# else:
#     print(False)

# 2
# if is_num(str1):
#     if float(str1) % 2 == 0:
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)

'''
2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，然后随机生成购买的斤数（5到10斤之间），最后计算出应该支付的金额！
'''

# price = input('橘子多少钱一斤？')
#
# if is_num(price):
#     price = float(price)
#     # 1
#     num = round(random.uniform(5, 10), 2)
#     # 2
#     num = round(random.random() + random.randint(5, 10), 2)
#     print('购买的斤数为：', num)
#
#     total_price = price * num
#     print('橘子的总价为：', round(total_price, 2))
# else:
#     print('请输入正确的数字')

'''
3、使用random模块和字符串拼接的方法，随机生成一个130开头的手机号码
'''
# 1
# tel = '130'+''.join(random.sample('1234567890', 8))
# print(tel)

# 2
# tel_str = ''
# i = 0
# while i < 8:
#     num = random.randint(0, 9)
#     tel_str = tel_str + str(num)
#     i += 1
#
# print('130'+tel_str)



'''
4、现有字符串    str1 = "PHP is the best programming language in the world! "
      要求一：将给定字符串的PHP替换为Python      
      要求二：替换以后，将字符串以空格为分割点进行分割得到一个列表
'''

# str1 = "PHP is the best programming language in the world! "
#
# str2 = str1.replace('PHP', 'Python')
# print(str2)
#
# list1 = str2.split(' ')
# print(list1)


'''
5、编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周X”（要求：使用上课学过的知识点来做）
'''
# week_num = input('请输入1-7之间的数字：')
#
# week_list = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
#
#
# def is_int(input_info):
#     try:
#         int(input_info)
#     except ValueError:
#         return False
#     else:
#         return True
#
#
# if is_int(week_num):
#     if 0 < int(week_num) < 8:
#         print('今天是{}'.format(week_list[int(week_num) - 1]))
#     else:
#         exit('输入的数字需要在1和7之间')
# else:
#     exit('请输入1-7之间的整数')
