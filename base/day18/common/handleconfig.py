"""
============================
Author:luli
time:2020/2/11
company:happy
============================
"""
import os
from configparser import ConfigParser
from common.handlepath import CONFDIR


class HandleConfig(ConfigParser):
    def __init__(self, filename):
        # 调用父类的init方法
        super().__init__()
        self.filename = filename
        self.read(filename, encoding='utf8')

    def write_data(self, session, key, value):
        self.set(session, key, value)
        self.write(fp=open(self.filename, 'w'))


conf = HandleConfig(os.path.join(CONFDIR, 'config.ini'))
