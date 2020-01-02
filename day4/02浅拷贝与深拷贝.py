"""
============================
Author:luli
Time:2020/1/2
Company:Happy
============================
"""
import copy

# name = 'moon'
# name1 = copy.copy(name)
# print(name, id(name))  # moon 2132306201776
# print(name1, id(name1))  # moon 2132306201776

li1 = [1, 2, 3, 4, {'name': 'luna'}]

li2 = li1.copy()

li2[4]['name'] = 'moon'

print(li1, id(li1))
# [1, 2, 3, 4, {'name': 'moon'}] 2163716106056
print(li2, id(li2))
# [1, 2, 3, 4, {'name': 'moon'}] 2163716106120