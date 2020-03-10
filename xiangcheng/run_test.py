"""
============================
Author:luli
Time:2020/3/9
Company:Happy
============================
"""
import os
import datetime
import unittest
from BeautifulReport import BeautifulReport
from common.handlepath import CASEDIR, REPORTDIR
from common.handle_email import send_email
from library.HTMLTestRunnerNew import HTMLTestRunner

date = datetime.datetime.now().strftime("%Y-%m-%d%H%M")
# 创建测试套件
suite = unittest.TestSuite()

# 将测试用例加载到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASEDIR))
# 创建测试运行程序
# report_file = os.path.join(REPORTDIR, 'report.html')
# runner = HTMLTestRunner(stream=open(report_file, 'wb'),
#                         title='享橙接口测试报告',
#                         description='随便测测',
#                         tester='鹿梨')
# # 执行测试运行程序
# runner.run(suite)

br = BeautifulReport(suite)

br.report("前程贷项目用例", filename=date + "report.html", report_dir=REPORTDIR)

# send_email(report_file, '享橙接口测试报告')
