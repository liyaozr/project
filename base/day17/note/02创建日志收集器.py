"""
============================
Author:luli
time:2020/2/12
company:happy
============================
"""

import logging

mylog = logging.getLogger('luli')

mylog.setLevel('DEBUG')

# 创建输出渠道
sh = logging.StreamHandler()
# 设置输出渠道的输出等级
sh.setLevel('INFO')
# 将输出渠道添加到收集器中
mylog.addHandler(sh)
# 创建输出渠道（输出到文件）
fh = logging.FileHandler(filename='log.log', encoding='utf8')
fh.setLevel('ERROR')
mylog.addHandler(fh)
# 定义一个格式
format = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'''
# 创建一个输出格式
fm = logging.Formatter(format)
# 将输出格式和输出渠道绑定
sh.setFormatter(fm)

mylog.debug('这是一条debug信息')
mylog.info('这是一条info信息')
mylog.warning('这是一条warning信息')
mylog.error('这是一条error信息')
mylog.critical('这是一条critical信息')
