"""
============================
Author:luli
Time:2020/1/2
Company:Happy
============================
"""

# index 返回该元素在列表中的下标位置，找不到会报错
# li = [1, 'mo', 3, 4, 5, 22, 1, 3, 1]
# print(li.index('mo'))  # 1
# print(li.index(1))  # 0，只返回第一个
# print(li.index(6))  # ValueError: 6 is not in list

# count 查找某个元素在列表中出现的次数
# li = [1, 'mo', 3, 4, 5, 22, 1, 3, 1]
# print(li.count(1))  # 3
# print(li.count(6))  # 0

# li = [1, 9, 3, 4, 5, 22, 1, 3, 1]
# li.sort()  # 没有返回值，直接在原列表上操作
# print(li)  # [1, 1, 1, 3, 3, 4, 5, 9, 22]
#
# li.reverse() # 没有返回值，直接在原列表上操作
# print(li) # [22, 9, 5, 4, 3, 3, 1, 1, 1]

li = [1, 9, 3]
li1 = li.copy()
print(li, id(li))  # [1, 9, 3] 2132369166856
print(li1, id(li1))  # [1, 9, 3] 2132369167368

