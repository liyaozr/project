"""
============================
Author:luli
time:2020/1/15
company:happy
============================
"""
import os


def func():
    print('python')


a = 100
# 这个条件只有在直接运行这个文件的时候才成立，模块导入的时候
if __name__ == '__mian__':
    print(a)
    func()

# print('__file__：', __file__)

print(os.path.dirname(__file__))
