"""
============================
Author:luli
time:2020/2/16
company:happy
============================
"""

import unittest
import os
from library.HTMLTestRunnerNew import HTMLTestRunner
from common.handlepath import CASEDIR, REPORTDIR

suite = unittest.TestSuite()

loader = unittest.TestLoader()

suite.addTest(loader.discover(CASEDIR))

runner = HTMLTestRunner(stream=open(os.path.join(REPORTDIR, 'report.html'), 'wb'),
                        title='注册测试报告',
                        description='这是项目搭建生成的报告',
                        tester='鹿梨')

runner.run(suite)
