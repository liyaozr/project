"""
============================
Author:luli
time:2020/1/15
company:happy
============================
"""

import os

dir = os.path.dirname(__file__)
dir_list = os.listdir()
# print(dir_list)
for item in dir_list:
    item_dir = os.path.join(dir + item)
    print(item_dir)

# 获取父级目录，一层一层往上取
# d1 = os.path.dirname(__file__)
#
# print(d1)
#
# d2 = os.path.dirname(d1)
# print(d2)

# 一行代码获取
# d1 = os.path.dirname(__file__)
# d2 = os.path.abspath(__file__)
# print(d1)
# print(d2)
#
# base_dir1 = os.path.dirname(os.path.dirname((os.path.dirname(__file__))))
# base_dir2 = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
# print(base_dir1)
# print(base_dir2)


# print(a)
# print(__file__)
# print(os.path.abspath(__file__))
