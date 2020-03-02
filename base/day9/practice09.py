"""
============================
Author:luli
time:2020/1/13
company:happy
============================
"""

# filter
# def func(item):
#     return item > 20
#
#
# li = [11, 22, 33, 44]
# res = filter(func, li)
# print(res)
# print(list(res))


# 打开文件
f = open('test.txt', 'r', encoding='utf8')

# 复制图片
f1 = open('test.png', 'rb')
content = f1.read()

f2 = open('test_copy.jpg', 'ab')
f2.write(content)
f1.close()
f2.close()
