"""
============================
Author:luli
time:2020/2/16
company:happy
============================
"""
import os
import unittest
from library.ddt import ddt, data
from common.readexcel import ReadExcel
from register import register
from common.handlelog import log
from common.handlepath import DATADIR


@ddt
class TestRegister(unittest.TestCase):
    excel = ReadExcel(os.path.join(DATADIR, 'cases.xlsx'), 'register')
    cases = excel.read_data()

    @data(*cases)
    def test_register(self, case):
        data = eval(case['data'])
        expected = eval(case['expected'])
        row = case['case_id'] + 1
        res = register(*data)

        try:
            self.assertEqual(expected, res)
        except AssertionError as E:
            self.excel.write_data(row=row, column=5, value='未通过')
            log.error('用例执行未通过')
            # 日志有一个专门记录捕获异常的方法
            log.exception(E)
            raise E
        else:
            self.excel.write_data(row=row, column=5, value='通过')
            log.info('用例{}执行通过'.format(case['title']))
