"""
============================
Author:luli
time:2020/1/24
company:happy
============================
"""
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from day14.task.testcases import LoginTest

datas = [
    {'data': ('python26', 'lemonban'), 'excepted': {"code": 0, "msg": "登录成功"}},
    {'data': ('python261', 'lemonban'), 'excepted': {"code": 1, "msg": "账号或密码不正确"}},
    {'data': ('python26', 'lemonban1'), 'excepted': {"code": 1, "msg": "账号或密码不正确"}},
    {'data': (None, 'lemonban'), 'excepted': {"code": 1, "msg": "所以的参数不能为空"}},
    {'data': ('python26', None), 'excepted': {"code": 1, "msg": "所以的参数不能为空"}}
]

suite = unittest.TestSuite()

for data in datas:
    case = LoginTest('test_login', data)
    suite.addTest(case)

runner = HTMLTestRunner(stream=open('report.html', 'wb'),
                        title='登陆测试报告',
                        description='这是一份关于登陆函数的测试报告',
                        tester='鹿梨')
runner.run(suite)
