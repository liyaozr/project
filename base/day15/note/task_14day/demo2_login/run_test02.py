"""
============================
Author:柠檬班-木森
Time:2020/2/5   20:16
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from py26_15day.task_14day.demo2_login.testcases import LoginTestCase
from HTMLTestRunnerNew import HTMLTestRunner

# 多条用例数据
cases = [
    {"excepted": {"code": 1, "msg": "注册成功"}, "data": ("python26", "lemonban")},
    {"excepted": {"code": 1, "msg": "所以的参数不能为空"}, "data": (None, "lemonban")},
    {"excepted": {"code": 1, "msg": "所以的参数不能为空"}, "data": ("python26", None)},
    {"excepted": {"code": 1, "msg": "账号或密码不正确"}, "data": ("python25", "lemonban")},
    {"excepted": {"code": 1, "msg": "账号或密码不正确"}, "data": ("python26", "lemonban111")},
]

# 创建测试套件
suite = unittest.TestSuite()

# loader = unittest.TestLoader() #  下面这种加载方式 不需要使用loader来加载
# 通过循环来遍历用例数据，每遍历出来一条数据，就创建一个用例对象，将用例对象添加到套件中
for case_data in cases:
    # 创建一条测试用例（一个测试用例对象）
    case = LoginTestCase("test_login", case_data)
    # 加载用例到套件
    suite.addTest(case)

# runner = unittest.TextTestRunner()

# 创建一个测试运行程序
runner = HTMLTestRunner(stream=open('report.html', 'wb'),
                        title='柠檬班测试报告',
                        description='demo1报告',
                        tester='MuSen')
runner.run(suite)
