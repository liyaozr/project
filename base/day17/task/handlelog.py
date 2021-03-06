"""
============================
Author:luli
time:2020/2/12
company:happy
============================
"""
import logging
from logging.handlers import TimedRotatingFileHandler


class HandleLog():

    @staticmethod
    def create_logger():
        # 创建收集器，设置收集器的等级
        mylog = logging.getLogger('luli')
        mylog.setLevel('DEBUG')

        # 创建输出到控制台的渠道，设置等级
        sh = logging.StreamHandler()
        sh.setLevel('DEBUG')
        mylog.addHandler(sh)

        # 创建输出到文件的渠道，设置等级
        # fh = logging.FileHandler(filename='logs.logs', encoding='utf8')
        fh = TimedRotatingFileHandler(filename='log.log',
                                      encoding='utf8',
                                      when='D',
                                      interval=1,
                                      backupCount=7)
        fh.setLevel('ERROR')
        mylog.addHandler(fh)

        # 设置日志输出格式
        formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        fm = logging.Formatter(formater)
        sh.setFormatter(fm)
        fh.setFormatter(fm)

        return mylog


log = HandleLog.create_logger()

log.debug("这个是debug等级的日志")
log.info("这个是info等级的日志")
log.warning("这个是warning等级的日志")
log.error("这个是error等级的日志")
log.critical("这个是critical等级的日志")
