"""
============================
Author:luli
time:2020/2/10
company:happy
============================
"""
import unittest
from ddt import ddt, data
from day16.task.register import register
from day16.task.readexcel import ReadExcel

# 写了@ddt之后，就会把这个类放到ddt中去改造
@ddt
class LoginTest(unittest.TestCase):
    excel = ReadExcel('cases.xlsx', 'register')
    cases = excel.read_data()

    # data里面放测试用例数据，每一个参数会自动生成一条测试用例
    @data(*cases)
    def test_login(self, case):

        data = eval(case['data'])
        expected = eval(case['expected'])
        res = register(*data)
        row = case["case_id"] + 1
        try:
            self.assertEqual(res, expected)
        except AssertionError as E:
            self.excel.write_data(row=row, column=5, value='测试未通过')
            raise E
        else:
            self.excel.write_data(row=row, column=5, value='测试通过')
