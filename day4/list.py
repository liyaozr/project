"""
============================
Author:luli
Time:2019/12/31
Company:Happy
============================
"""

li1 = [1, 2, 3, 4, {'name': 'luna'}]

li2 = li1.copy()

li2[4]['name'] = 'moon'

print(li1, id(li1))
print(li2, id(li2))
