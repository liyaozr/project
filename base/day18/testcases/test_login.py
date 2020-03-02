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
from common.handlepath import DATADIR
from common.handlelog import log
from login import login_check


@ddt
class TestLogin(unittest.TestCase):
    excel = ReadExcel(os.path.join(DATADIR, 'cases.xlsx'), 'login')
    cases = excel.read_data()

    @data(*cases)
    def test_login(self, case):
        data = eval(case['data'])
        expected = eval(case['expected'])
        row = case['case_id'] + 1
        res = login_check(*data)
        try:
            self.assertEqual(expected, res)
        except AssertionError as E:
            self.excel.write_data(row=row, column=5, value='不通过')
            log.error('{}测试不通过'.format(case['title']))
            log.exception(E)
            raise E
        else:
            self.excel.write_data(row=row, column=5, value='通过')
            log.info('{}测试通过'.format(case['title']))
