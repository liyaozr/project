"""
============================
Author:柠檬班-木森
Time:2020/2/5   20:16
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from py26_14day.demo01.testcases import RegisterTestCase
from HTMLTestRunnerNew import HTMLTestRunner


# 单独一条用例数据
case_data1 = {"excepted": {"code": 1, "msg": "注册成功"},
              "data": ('python1', '123456', '123456')
              }

# 创建测试套件
suite = unittest.TestSuite()

# 创建一条测试用例（一个测试用例对象）
case = RegisterTestCase("test_register", case_data1)
# 加载用例到套件
suite.addTest(case)

# 创建一个测试运行程序
runner = HTMLTestRunner(stream=open('demo1_report.html', 'wb'),
                        title='柠檬班测试报告',
                        description='demo1报告',
                        tester='MuSen')
runner.run(suite)
