'''
============================
Author:luli
time:2020/1/6
company:happy
============================
'''

import random

'''
1、 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？
'''
# 方法1
# height = 100
# result = 0
# i = 0
# while i < 10:
#     if i == 0:
#         result = result + height
#         print('第{}次落地总共经过'.format(i + 1), result)
#     else:
#         result = result + height * 2
#         print('第{}次落地总共经过'.format(i + 1), result)
#     height = height / 2
#     i += 1
# print(result)

# 方法2
# height = 50
# result = 100
# i = 1
# while i < 10:
#     result = result + height * 2
#     height = height / 2
#     i += 1
# print(result)

# 方法3
# height = 100
# result = -100
# for i in range(10):
#     result = result + height * 2
#     height = height / 2
#     i += 1
# print(result)

'''
2、猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半  在加一个。到第10天早上想再吃时，见只剩下一个桃子了。
请通过一段通过代码来计算第一天摘了多少个桃子？
'''
# 方法1
# peach = 1
# i = 10
# print('第{}天的桃子有{}个'.format(i, peach))
# while i > 1:
#     i = i - 1
#     peach = (peach + 1) * 2
#     print('第{}天的桃子有{}个'.format(i, peach))


# 方法2
# peach = 1
# i = 0
# for i in range(9):
#     peach = (peach + 1) * 2
# print(peach)


'''
3、使用循环和条件语对剪刀石头布游戏进行升级，提示用户输入要出的拳 ：
石头（1）／剪刀（2）／布（3）/退出（4）
电脑随机出拳比较胜负，显示 用户胜、负还是平局，打印结果，一轮游戏完了之后，
重新回到用户输入的步骤，直到用户输入4退出游戏，如下图所示：
'''

# while True:
#     input_num = int(input('请输入出拳数字：石头（1）／剪刀（2）／布（3）/退出（4）'))
#     random_num = random.randint(1, 3)
#     print(random_num)
#     if input_num > 4 or input_num < 1:
#         print('你输入的数字有误')
#     elif input_num == 4:
#         exit('-----您选择退出游戏------')
#     elif input_num - random_num == -1 or input_num - random_num == 2:
#         print('你赢了')
#     elif input_num - random_num == -2 or input_num - random_num == 1:
#         print('你输了')
#     else:
#         print('平局')
