"""
============================
Author:柠檬班-木森
Time:2020/2/3   21:57
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from py26_13day.login import login_check


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

    def setUp(self):
        print("该方法在每一条测试用例执行之前会调用")

    def tearDown(self):
        print("该方法在每一条测试用例执行之后会调用")

    @classmethod
    def setUpClass(cls):
        print("该方法在测试类中的用例执行之前会调用")

    @classmethod
    def tearDownClass(cls):
        print("该方法在测试类中的所有用例执行之后会调用")



if __name__ == '__main__':
    unittest.main()
