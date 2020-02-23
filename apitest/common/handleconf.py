"""
============================
Author:luli
time:2020/2/23
company:happy
============================
"""
import os
from configparser import ConfigParser
from common.handlepath import CONFDIR


class HandleConf(ConfigParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.read(filename, encoding='utf8')

    def write_data(self, session, key, value):
        self.set(session, key, value)
        self.write(fp=open(self.filename, 'wb'))


conf = HandleConf(os.path.join(CONFDIR, "config.ini"))
