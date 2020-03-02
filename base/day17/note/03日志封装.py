"""
============================
Author:luli
time:2020/2/12
company:happy
============================
"""
import logging


def creat_logger():
    mylog = logging.getLogger('luli')
    mylog.setLevel('DEBUG')

    # 创建输出到控制台的渠道，设置等级
    sh = logging.StreamHandler()
    sh.setLevel('DEBUG')
    mylog.addHandler(sh)

    # 创建输出渠道（输出到文件），设置等级
    fh = logging.FileHandler(filename='log.log', encoding='utf8')
    fh.setLevel('DEBUG')
    mylog.addHandler(fh)

    # 设置日志输出格式
    formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'''
    fm = logging.Formatter(formater)
    sh.setFormatter(fm)
