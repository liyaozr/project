"""
============================
Author:柠檬班-木森
Time:2020/1/6   21:30
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
需求：1、计算1+2+3+4+。。。。100的结果


内置函数range:
range(n):默认生成一个 0到n-1的整数序列，对于这个整数序列，我们可以通过list()函数转化为列表类型的数据。

range（n,m)：默认生成一个n到m-1的整数序列，对于这个整数序列，我们可以通过list()函数转化为列表类型的数据。

range(n,m,k)：相当于其他函数里面的for循环。n 初始值  m 结束值 ， k 步长，会生成初始值为n,结束值为m-1,递减或者是递增的整数序列。

range返回的数据是支持使用for进行遍历的,也能够进行下标取值 和切片（切片返回的还是range类型的数据）


"""
# print(list(range(10)))
# r = range(1,101)
# print(r[:10])
# print(list(r))

# print(list(range(1,101,5)))


#  while循环实现
# i = 1
# s = 0
# while i <= 100:
#     s = s + i
#     i += 1
#
# print(s)

# s = 0
# for i in range(1, 101):
#     s = s +i
# print(s)


"""
需求二：使用for打印100遍hello python

需求三：打印到第50遍之后 后面的不再打印

for循环也支持使用break,continue



"""

for i in range(100):
    print("这是第{}遍打印：hello python".format(i + 1))
    if i + 1 == 50:
        continue
    print("------------------------end：{}------------------------".format(i+1))
