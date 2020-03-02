"""
============================
Author:luli
time:2020/2/11
company:happy
============================
"""
from configparser import ConfigParser

'''
1、将register这个函数的测试改成ddt去实现（参照上课的login）
2、根据上课的提示完成配置文件类的封装，提示如下：
配置文件类的封装
封装的目的：使用更简单
封装的需求：
1、简化创建配置文件解析器对象，加载配置文件的流程（需要封装），提示（重写init方法）
2、读取数据（不进行封装，使用原来的方法），通过继承父类即可
3、简化写入数据的操作（需要封装），提示：自定义一个write_data方法。
class Config():
    pass
'''


class Config(ConfigParser):
    def __init__(self, filename):
        # 调用父类的init方法
        super().__init__()
        self.filename = filename
        self.read(filename)

    def write_data(self, session, key, value):
        self.set(session, key, value)
        self.write(fp=open(self.filename, 'w'))


test1 = Config('conf.ini')
test1.write_data('mysql', 'user', 1234)
