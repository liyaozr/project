"""
============================
Author:luli
time:2020/2/10
company:happy
============================
"""
import unittest
from day15.task.readexcel import ReadExcel
from day15.task.testcases import LoginTest, RegisterTest
from HTMLTestRunnerNew import HTMLTestRunner

# 第一步，创建测试套件
suite = unittest.TestSuite()

# 读取数据
excel = ReadExcel('cases.xlsx', 'login')
case_datas = excel.read_data()

# 第二步：加载测试用例到套件
for case_data in case_datas:
    case = LoginTest('test_login', case_data)
    suite.addTest(case)

excel = ReadExcel('cases.xlsx', 'register')
case_datas = excel.read_data()

for case_data in case_datas:
    case = RegisterTest('test_register', case_data)
    suite.addTest(case)

# 第三步：执行测试运行程序
runner = HTMLTestRunner(stream=open('report.html', 'wb'))
runner.run(suite)
