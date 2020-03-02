"""
============================
Author:柠檬班-木森
Time:2020/02/05
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from py26_14day.task_13day import testcases

# 创建测试套件
suite = unittest.TestSuite()

# 添加一个模块中所有的测试用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(testcases))

# 生成html文件的的测试报告


runner = HTMLTestRunner(stream=open('zy_report.html', 'wb'),
                        title='柠檬班测试报告',
                        description='这是我们26期的第一次生成报告的作业',
                        tester='MuSen')

runner.run(suite)
