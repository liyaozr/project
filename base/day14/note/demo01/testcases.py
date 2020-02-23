"""
============================
Author:柠檬班-木森
Time:2020/02/05
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest

from py26_14day.task_13day.register import register


class RegisterTestCase(unittest.TestCase):

    def __init__(self, methodName, case_data):
        self.case_data = case_data
        # 调用父类的init的方法
        super().__init__(methodName)

    def test_register(self):
        # 第一步：准备用例的数据
        # 预期结果：
        excepted = self.case_data["excepted"]
        # 参数：data
        data = self.case_data["data"]
        # 第二步：调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        # 第三步：断言（比对预期结果和实际结果）
        self.assertEqual(excepted, res)
