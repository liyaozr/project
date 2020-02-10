"""
============================
Author:柠檬班-木森
Time:2020/2/7   21:29
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from py26_15day.demo2.register import register
from py26_15day.demo2.login import login_check
from py26_15day.demo2.readexcel import ReadExcel


class RegisterTestCase(unittest.TestCase):
    excel = ReadExcel("cases.xlsx", "register")

    def __init__(self, methodName, case_data):
        self.case_data = case_data
        # 调用父类的init的方法
        super().__init__(methodName)

    def test_register(self):
        # 第一步：准备用例的数据
        # 预期结果：
        excepted = eval(self.case_data["expected"])
        # 参数：data
        data = eval(self.case_data["data"])
        # 用例所在行
        row = self.case_data["case_id"] + 1

        # 第二步：调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        # 第三步：断言（比对预期结果和实际结果）
        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            # 在excel中写入用例未通过
            self.excel.write_data(row=row, column=5, value="未通过")
            raise e
        else:
            # 在excel中写入用例通过
            self.excel.write_data(row=row, column=5, value="通过")


class LoginTestCase(unittest.TestCase):
    excel = ReadExcel("cases.xlsx", "login")

    def __init__(self, methodName, case_data):
        self.case_data = case_data
        # 调用父类的init的方法
        super().__init__(methodName)

    def test_login(self):
        # 第一步：准备用例的数据
        # 预期结果：
        expected = eval(self.case_data["expected"])
        # 参数：data
        data = eval(self.case_data["data"])
        # 用例所在行
        row = self.case_data["case_id"] + 1
        # 第二步：调用被测试的功能函数，传入参数，获取实际结果：
        res = login_check(*data)
        # 第三步：断言（比对预期结果和实际结果）
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            # 在excel中写入用例未通过
            self.excel.write_data(row=row, column=5, value="未通过")
            raise e
        else:
            # 在excel中写入用例通过
            self.excel.write_data(row=row, column=5, value="通过")
