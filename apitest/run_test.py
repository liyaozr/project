"""
============================
Author:luli
time:2020/2/23
company:happy
============================
"""
import os
import unittest
from common.handlepath import CASEDIR, REPORTDIR
from library.HTMLTestRunnerNew import HTMLTestRunner

# 创建测试套件
suite = unittest.TestSuite()

# 将测试用例加载到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASEDIR))

# 创建测试运行程序
report_file = os.path.join(REPORTDIR, 'report.html')
runner = HTMLTestRunner(stream=open(report_file, 'wb'),
                        title='第一次接口测试报告',
                        description='这是一份关于登陆、注册的接口测试报告',
                        tester='鹿梨')
# 执行测试运行程序
runner.run(suite)
