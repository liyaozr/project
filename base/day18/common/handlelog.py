"""
============================
Author:luli
time:2020/2/12
company:happy
============================
"""
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from common.handleconfig import conf
from common.handlepath import LOGDIR


class HandleLog():

    @staticmethod
    def create_logger():
        # 创建收集器，设置收集器的等级
        mylog = logging.getLogger(conf.get('log', 'name'))
        mylog.setLevel(conf.get('log', 'level'))

        # 创建输出到控制台的渠道，设置等级
        sh = logging.StreamHandler()
        sh.setLevel(conf.get('log', 'sh_level'))
        mylog.addHandler(sh)

        # 创建输出到文件的渠道，设置等级
        # fh = logging.FileHandler(filename='logs.logs', encoding='utf8')
        fh = TimedRotatingFileHandler(filename=os.path.join(LOGDIR, 'log.log'),
                                      encoding='utf8',
                                      when='D',
                                      interval=1,
                                      backupCount=7)
        fh.setLevel(conf.get('log', 'fh_level'))
        mylog.addHandler(fh)

        # 设置日志输出格式
        formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        fm = logging.Formatter(formater)
        sh.setFormatter(fm)
        fh.setFormatter(fm)

        return mylog


log = HandleLog.create_logger()
