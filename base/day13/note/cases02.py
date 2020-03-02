"""
============================
Author:柠檬班-木森
Time:2020/2/3   20:58
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from day13.note.login import login_check


class LoginTest(unittest.TestCase):

    def test_login_pass(self):
        # 正常登录
        # 第一步：准备用例数据
        # 入参
        data = ("python26", "lemonban")
        # 预期结果
        expected = {"code": 0, "msg": "登录成功"}

        # 第二步：获取实际结果
        # 实际结果(传入参数，调用待测试的功能函数)
        res = login_check(*data)

        # 第三步：比较预期结果和实际结果（断言）
        self.assertEqual(expected, res)

    def test_user_is_none(self):
        # 账号为空
        # 入参
        data = (None, "lemonban")
        # 预期结果
        expected = {"code": 1, "msg": "所以的参数不能为空"}

        # 第二步：获取实际结果
        # 实际结果(传入参数，调用待测试的功能函数)
        res = login_check(*data)

        # 第三步：比较预期结果和实际结果（断言）
        self.assertEqual(expected, res)

    def test_pwd_is_none(self):
        # 账号为空
        # 入参
        data = ("python26", None)
        # 预期结果
        expected = {"code": 1, "msg": "所以的参数不能为空"}

        # 第二步：获取实际结果
        # 实际结果(传入参数，调用待测试的功能函数)
        res = login_check(*data)

        # 第三步：比较预期结果和实际结果（断言）
        self.assertEqual(expected, res)

    def test_user_error(self):
        # 账号错误
        # 第一步：准备用例数据
        # 入参
        data = ("python25", "lemonban")
        # 预期结果
        expected = {"code": 1, "msg": "账号或密码不正确"}

        # 第二步：获取实际结果
        # 实际结果(传入参数，调用待测试的功能函数)
        res = login_check(*data)

        # 第三步：比较预期结果和实际结果（断言）
        self.assertEqual(expected, res)

    def test_pwd_error(self):
        # 账号错误
        # 第一步：准备用例数据
        # 入参
        data = ("python26", "lemonban111")
        # 预期结果
        expected = {"code": 1, "msg": "账号或密码不正确"}

        # 第二步：获取实际结果
        # 实际结果(传入参数，调用待测试的功能函数)
        res = login_check(*data)

        # 第三步：比较预期结果和实际结果（断言）
        self.assertEqual(expected, res)

    def test_pwd_error2(self):
        # 账号错误
        # 第一步：准备用例数据
        # 入参
        data = ("python26", "lemonban111")
        # 预期结果
        expected = {"code": 1, "msg": "账号或密码不正确"}

        # 第二步：获取实际结果
        # 实际结果(传入参数，调用待测试的功能函数)
        res = login_check(*data)

        # 第三步：比较预期结果和实际结果（断言）
        self.assertEqual(expected, res)

# 创建测试用例对象的时候，必须要传入用例的方法名
# case1 = LoginTest("test_login_pass")
#
# case2 = LoginTest("test_user_is_none")
