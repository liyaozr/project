"""
============================
Author:luli
time:2020/2/10
company:happy
============================
"""

import unittest
from HTMLTestRunnerNew import HTMLTestRunner

# 第一步：创建测试套件
suite = unittest.TestSuite()

# 第二：加载用例到套件
from day16.demo1 import testcases

loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(testcases))

# 第三步：执行测试用例（先创建测试运行程序）
# 创建测试运行程序
runner = HTMLTestRunner(stream=open("report.html", "wb"),
                        title="py26期第一份报告",
                        description="上课生成的测试报告",
                        tester="鹿梨")

# 执行测试套件中的测试用例
runner.run(suite)
