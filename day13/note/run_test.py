"""
============================
Author:柠檬班-木森
Time:2020/2/3   21:46
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import unittest
from HTMLTestRunnerNew import HTMLTestRunner

# 第一步：创建测试套件
suite = unittest.TestSuite()

# 第二：加载用例到套件
from day13.note import testcases

loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(testcases))

# 第三步：执行测试用例（先创建测试运行程序）
# 创建测试运行程序
runner = HTMLTestRunner(stream=open("report.html", "wb"),
                        title="py26期第一份报告",
                        description="上课生成的测试报告",
                        tester="musen")

# 执行测试套件中的测试用例
runner.run(suite)
