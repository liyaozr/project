"""
============================
Author:luli
time:2020/2/23
company:happy
============================
"""
import random


def random_phone():
    random_num = ''.join(random.sample('0123456789', 8))
    phone = '130' + random_num
    return phone


print(random_phone())
