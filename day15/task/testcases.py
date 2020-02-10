"""
============================
Author:luli
time:2020/1/24
company:happy
============================
"""

import unittest
from day15.task.login import login_check
from day15.task.register import register
from day15.task.readexcel import ReadExcel

'''
1、完成excel类封装（提交）

2、完整上课的demo2案例，所需资料在附件中（提交）

3、建议把上课的代码敲三遍（不用提交）
'''


class LoginTest(unittest.TestCase):
    # 创建文件对象
    excel = ReadExcel("cases.xlsx", "login")

    def __init__(self, method, data):
        self.datas = data
        super().__init__(method)

    def test_login(self):
        # 准备数据
        data = eval(self.datas['data'])
        expected = eval(self.datas['expected'])
        res = login_check(*data)
        # 获取case_id这一列的值，方便用于写入数据
        row = self.datas["case_id"] + 1
        try:
            self.assertEqual(res, expected)
        except AssertionError as E:
            # 在excel中写入用例未通过
            self.excel.write_data(row=row, column=5, value='测试未通过')
            # 抛出异常
            raise E
        else:
            # 在excel中写入用例通过
            self.excel.write_data(row=row, column=5, value='测试通过')


class RegisterTest(unittest.TestCase):
    excel = ReadExcel("cases.xlsx", "register")

    def __init__(self, method, data):
        self.datas = data
        super().__init__(method)

    def test_register(self):
        data = eval(self.datas['data'])
        expected = eval(self.datas['expected'])
        res = register(*data)
        row = self.datas["case_id"] + 1
        try:
            self.assertEqual(res, expected)
        except AssertionError as E:
            self.excel.write_data(row=row, column=5, value='测试未通过')
            raise E
        else:
            self.excel.write_data(row=row, column=5, value='测试通过')
