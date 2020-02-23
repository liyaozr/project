"""
============================
Author:柠檬班-木森
Time:2020/2/12   21:47
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import unittest
from ddt import ddt,data
from py26_17day.demo5.readexcel import ReadExcel
from py26_17day.demo5.register import register
from py26_17day.demo5.handlelog import log

@ddt
class TestRegister(unittest.TestCase):
    excel = ReadExcel("cases.xlsx","register")
    cases = excel.read_data()

    @data(*cases)
    def test_register(self,case):

        # 第一步：准备数据
        data = eval(case["data"])
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        # 第二步：传入参数，调用待测的函数，获取实际结果
        res = register(*data)
        # 第三步：数据比对
        try:
            self.assertEqual(expected,res)
        except AssertionError as e:
            self.excel.write_data(row=row,column=5,value="未通过")
            log.error("用例:{}执行未通过".format(case["title"]))
            raise e
        else:
            self.excel.write_data(row=row, column=5, value="通过")
            log.info("用例:{}执行通过".format(case["title"]))


