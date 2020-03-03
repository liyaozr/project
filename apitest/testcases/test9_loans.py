"""
============================
Author:luli
Time:2020/3/3
Company:Happy
============================
"""

import os
import unittest
import jsonpath
from library.ddt import ddt, data
from common.readexcel import ReadExcel
from common.handlepath import DATADIR
from common.handleconf import conf
from common.handlelog import log
from common.handlerequest import SendRequest
from common.handledata import CaseData

case_file = os.path.join(DATADIR, 'apicases.xlsx')


@ddt
class TestLoans(unittest.TestCase):
    excel = ReadExcel(case_file, 'loans')
    datas = excel.read_data()
    request = SendRequest()

    @classmethod
    def setUpClass(cls):
        data = {
            'mobile_phone': conf.get('test_data', 'phone'),
            'pwd': conf.get('test_data', 'pwd')
        }
        url = conf.get('env', 'url') + '/member/login'
        method = 'post'
        headers = eval(conf.get('env', 'headers'))
        response = cls.request.send(url=url, method=method, headers=headers, json=data)
        res = response.json()
        token = jsonpath.jsonpath(res, "$..token")[0]
        token_type = jsonpath.jsonpath(res, "$..token_type")[0]
        CaseData.token_value = token_type + " " + token

    @data(*datas)
    def test_loans(self, case):
        # 准备数据
        url = conf.get('env', 'url') + case['url']
        method = case['method']
        headers = eval(conf.get('env', 'headers'))
        headers['Authorization'] = getattr(CaseData, 'token_value')
        params = case['params']
        expected = eval(case['expected'])
        row = case['case_id'] + 1

        # 获取结果
        response = self.request.send(url=url, method=method, headers=headers, params=params)
        res = response.json()

        # 对预期结果和响应结果进行断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
        except AssertionError as E:
            print('预期结果：', expected['msg'])
            print('实际结果：', res['msg'])
            self.excel.write_data(row=row, column=7, value='不通过')
            log.error('{}用例不通过'.format(case['title']))
            log.exception(E)
            raise E
        else:
            self.excel.write_data(row=row, column=7, value='通过')
