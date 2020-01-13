"""
============================
Author:柠檬班-木森
Time:2020/1/10   21:44
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

# li = [11, 22, 33, 44, 55, 6, 6721, 34, 5, 67, 8, 3, 7, 22, 7, 4]

# 最大值
# res = max(li)
# print(res)

# 最小值
# res2 = min(li)
# print(res2)
# 求和
# s = sum(li)
# print(s)


#  高级的内置函数
li1 = (11, 22, 331, 21, 322)
dic = {"a": 11, "b": 333}

# enumerate：利用它可以同时获得索引和值
# res = enumerate(dic)
# for i in res:
#     print(i)


# eval：识别字符串中有效的python表达式
str1 = "{'a':11,'b':22}"
str2 = "[11,22,33,44]"

# 把str1转换为字典  ，str2转换为列表

# dic1 = eval(str1)
# print(dic1, type(dic1))
#
# li = eval(str2)
# print(li, type(li))

a = 1000
b = 10

# s1 = "a > b"
# print(eval(s1))

# s2 = "print('python26')"
# eval(s2)    #====> print('python26')
# print('python26')

# # zip：聚合打包
# li = [1, 2, 3, 4]
# li2 = [11, 22, 33, 44]
# li3 = [111, 222, 333]
#
# res = zip(li, li2, li3)
# print(list(res))

#  zip的应用场景：
title = ["aa", "bb", "cc"]
value = [11, 22, 33]

# 注意点：zip打包之后返回的数据，只能使用一次
res = zip(title, value)

print(dict(res))
# print(list(res))

# filter
