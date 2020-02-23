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

# 多条用例数据
cases = [
    {"excepted": {"code": 1, "msg": "注册成功"}, "data": ('python1', '123456', '123456')},
    {"excepted": {"code": 0, "msg": "两次密码不一致"}, "data": ('python1', '1234567', '123456')},
    {"excepted": {"code": 0, "msg": "该账户已存在"}, "data":  ('python18', '1234567', '123456')},

]

# 创建测试套件
suite = unittest.TestSuite()

# 通过循环来遍历用例数据，每遍历出来一条数据，就创建一个用例对象，将用例对象添加到套件中
for case_data in cases:
    # 创建一条测试用例（一个测试用例对象）
    case = RegisterTestCase("test_register", case_data)
    # 加载用例到套件
    suite.addTest(case)

# 创建一个测试运行程序
runner = HTMLTestRunner(stream=open('demo1_report.html', 'wb'),
                        title='柠檬班测试报告',
                        description='demo1报告',
                        tester='MuSen')
runner.run(suite)
