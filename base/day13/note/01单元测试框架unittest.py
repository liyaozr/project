"""
============================
Author:柠檬班-木森
Time:2020/2/3   20:07
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import unittest
from day13.note.login import login_check

"""
定义测试用例类：只要定义的类继承于unittest.TestCase那么这个类就是测试用例类
测试用例怎么写：在测试用例类中定义以test开头的方法就是一条测试用例
unittest中评判断言是否通过的标准：是否出现断言错误
"""


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


# if __name__ == '__main__':
#     unittest.main()
