"""
============================
Author:luli
time:2020/1/24
company:happy
============================
"""

import unittest

from day13.register import register


class RegisterTest(unittest.TestCase):
    def test_register_success(self):
        # 注册成功
        # 第一步：准备用例数据
        data = ("caroline", "123456", "123456")
        expected = {"code": 1, "msg": "注册成功"}

        # 第二步：获取实际结果
        # 实际结果(传入参数，调用待测试的功能函数)
        res = register(*data)

        # 第三步：比较预期结果和实际结果（断言）
        self.assertEqual(expected, res)

    def test_user_is_empty(self):
        # 用户名为空
        data = ("", "123456", "123456")
        expected = {"code": 0, "msg": "所有参数不能为空"}
        res = register(*data)
        self.assertEqual(expected, res)

    def test_pwd1_is_empty(self):
        # 密码1为空
        data = ("caroline", "", "123456")
        expected = {"code": 0, "msg": "所有参数不能为空"}
        res = register(*data)
        self.assertEqual(expected, res)

    def test_pwd2_is_empty(self):
        # 密码2为空
        data = ("caroline", "123456", "")
        expected = {"code": 0, "msg": "所有参数不能为空"}
        res = register(*data)
        self.assertEqual(expected, res)

    def test_pwd_not_match(self):
        # 两次密码不一致
        data = ("caroline", "12345678", "123456")
        expected = {"code": 0, "msg": "两次密码不一致"}
        res = register(*data)
        self.assertEqual(expected, res)

    def test_user_exist(self):
        # 该账户已存在
        data = ("python26", "12345678", "12345678")
        expected = {"code": 0, "msg": "该账户已存在"}
        res = register(*data)
        self.assertEqual(expected, res)

    def test_user_too_long(self):
        data = ("carolinecarolinecaroline", "12345678", "12345678")
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        res = register(*data)
        self.assertEqual(expected, res)

    def test_user_too_short(self):
        data = ("lily", "12345678", "12345678")
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        res = register(*data)
        self.assertEqual(expected, res)

    def test_pwd_too_long(self):
        data = ("caroline", "123456789123456789123", "123456789123456789123")
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        res = register(*data)
        self.assertEqual(expected, res)

    def test_psw_too_short(self):
        data = ("caroline", "123", "123")
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        res = register(*data)
        self.assertEqual(expected, res)
