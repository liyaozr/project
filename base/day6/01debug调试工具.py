"""
============================
Author:柠檬班-木森
Time:2020/1/6   20:22
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
debug调试工具的使用

F8：遇到函数调用，不会进入到函数内部

F7：遇到函数调用，会进入到函数内部，一步一步执行

打断点：行号后面，点一下会出现一个红点

打了断点之后，使用debug模式去运行（运行到断点处会暂停）


"""

a = 100

b = 200
c = 300
d = 400
f = 80
y = (11, 22, 33)
dic = {"a": 111, "b": 222, "name": "musen"}
li = [11, 22, 33, 44]
s = {11,22,33,44}
print('---------------')

# import random
#
# print('---石头剪刀布游戏开始----')
# print('请按下面提示出拳：石头【1】 剪刀【2】 布【3】')
# user_num = int(input('请输入你的选项：'))
# # 电脑随机生成数字
# r_num = random.randint(1, 3)
# if 1 <= user_num <= 3:
#     # 判断用户和电脑是否相等
#     if r_num == user_num:
#         print('您的出拳为:{}，电脑出拳:{}，平局'.format(user_num, r_num))
#     # 判断用户胜利的情况
#     elif (user_num - r_num) == -1 or (user_num - r_num) == 2:
#         print('您的出拳为:{}，电脑出拳:{}，您胜利了'.format(user_num, r_num))
#     else:
#         print('您的出拳为:{}，电脑出拳:{}，您输了'.format(user_num, r_num))
# else:
#     print('您出拳有误，请按规矩出拳')
