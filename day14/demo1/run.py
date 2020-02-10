"""
============================
Author:luli
time:2020/1/24
company:happy
============================
"""

import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from day14.demo1.testcases import RegisterTest

cases = [
    {"excepted": {"code": 1, "msg": "注册成功"}, "data": ('python1', '123456', '123456')},
    {"excepted": {"code": 0, "msg": "两次密码不一致"}, "data": ('python12', '1234567', '123456')},
    {"excepted": {"code": 0, "msg": "该账户已存在"}, "data": ('python1', '1234567', '123456')},

]

# 第一步：创建测试套件
suite = unittest.TestSuite()

# 第二：加载用例到套件
for item in cases:
    case = RegisterTest('test_register_success', item['data'], item['excepted'])
    suite.addTest(case)

# 第三步：执行测试用例（先创建测试运行程序）
# 创建测试运行程序
runner = HTMLTestRunner(stream=open("report.html", "wb"),
                        title="注册测试报告",
                        description="关于注册功能的测试报告",
                        tester="鹿梨")

# 执行测试套件中的测试用例
runner.run(suite)
