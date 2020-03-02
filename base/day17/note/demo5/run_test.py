"""
============================
Author:柠檬班-木森
Time:2020/2/12   21:55
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from py26_17day.demo5 import testcases
from HTMLTestRunnerNew import HTMLTestRunner

# 第一步：创建套件
suite = unittest.TestSuite()

# 第二步：添加用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(testcases))


# 第三步：创建一个测试运行程序，执行套件中的用例
runner = HTMLTestRunner(stream=open("report.html","wb"),
                        title="26期知识梳理",
                        description='998899',
                        tester="木森"
                        )

runner.run(suite)
