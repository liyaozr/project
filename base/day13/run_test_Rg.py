"""
============================
Author:luli
time:2020/1/24
company:happy
============================
"""

import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from day13 import test_register

# 第一步：创建测试套件
suite = unittest.TestSuite()

# 第二：加载用例到套件


loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_register))

# 第三步：执行测试用例（先创建测试运行程序）
# 创建测试运行程序
runner = HTMLTestRunner(stream=open("report.html", "wb"),
                        title="注册测试报告",
                        description="关于注册功能的测试报告",
                        tester="鹿梨")

# 执行测试套件中的测试用例
runner.run(suite)
