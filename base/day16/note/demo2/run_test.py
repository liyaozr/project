"""
============================
Author:柠檬班-木森
Time:2020/2/7   21:32
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from py26_16day.demo2.readexcel import ReadExcel
from py26_16day.demo2.testcases import LoginTestCase,RegisterTestCase
from HTMLTestRunnerNew import HTMLTestRunner

# 第一步：创建测试套件
suite = unittest.TestSuite()


# 第二步：加载用例到套件
# 1、读取用例中的数据(登录)
excel= ReadExcel("cases.xlsx", "login")
case_datas1 = excel.read_data()
# 2、遍历数据，创建用例对象，将用例添加到套件
for case_data in case_datas1:
    case = LoginTestCase("test_login",case_data)
    suite.addTest(case)


# # 1、读取用例中的数据（注册）
excel= ReadExcel("cases.xlsx","register")
case_datas1 = excel.read_data()
# 2、遍历数据，创建用例对象，将用例添加到套件
for case_data in case_datas1:
    case = RegisterTestCase("test_register",case_data)
    suite.addTest(case)


# 第三步：创建测试运行程序，执行套件中的用例
runner = HTMLTestRunner(stream=open("report.html","wb"))

runner.run(suite)

