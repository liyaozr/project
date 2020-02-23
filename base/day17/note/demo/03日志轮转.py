"""
============================
Author:柠檬班-木森
Time:2020/2/12   21:17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import logging

from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# 第一步：创建一个日志收集器对象
mylog = logging.getLogger("musen")

# 第二步：设置日志收集器收集的等级
mylog.setLevel("DEBUG")

# 第三步：日志输出渠道的等级

# 创建一个根据文件大小进行轮转的输出渠道
fh = RotatingFileHandler(filename="mylog.log",
                         encoding="utf8",
                         maxBytes=1024,
                         backupCount=3
                         )
# # 创建一个根据时间进行轮转的收集器
# fh = TimedRotatingFileHandler(filename='my.logs',
#                               encoding='utf8',
#                               when='S',
#                               interval=1,
#                               backupCount=3)

# 设置输出等级
fh.setLevel("DEBUG")
# 添加到收集器中
mylog.addHandler(fh)

formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
# 创建一个输出格式
fm = logging.Formatter(formater)
# 将输出格式和输出渠道绑定
fh.setFormatter(fm)

mylog.debug("这个是debug等级的日志")
mylog.info("这个是info等级的日志")

mylog.warning("这个是warning等级的日志")
mylog.error("这个是error等级的日志")
mylog.critical("这个是critical等级的日志")
