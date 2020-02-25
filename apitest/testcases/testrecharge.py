"""
============================
Author:luli
time:2020/2/23
company:happy
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

case_file = os.path.join(DATADIR, 'apicases.xlsx')


@ddt
class TestRecharge(unittest.TestCase):
    excel = ReadExcel(case_file, 'recharge')
    datas = excel.read_data()
    request = SendRequest()

    @classmethod
    def setUpClass(cls):
        data = {"mobile_phone": "13058640001", "pwd": "lemonban"}
        url = conf.get('env', 'url') + '/member/login'
        method = 'post'
        headers = eval(conf.get('env', 'headers'))
        response = cls.request.send(url=url, method=method, headers=headers, json=data)
        res = response.json()
        token = jsonpath.jsonpath(res, "$..token")[0]
        token_type = jsonpath.jsonpath(res, "$..token_type")[0]
        cls.token_value = token_type + " " + token
        cls.member_id = jsonpath.jsonpath(res, "$..id")[0]

    @data(*datas)
    def test_recharge(self, case):
        # 准备数据
        url = conf.get('env', 'url') + case['url']
        method = case['method']
        headers = eval(conf.get('env', 'headers'))
        headers['Authorization'] = self.token_value
        case['data'] = case['data'].replace('#member_id#', str(self.member_id))
        data = eval(case['data'])
        expected = eval(case['expected'])
        row = case['case_id'] + 1
        # 获取结果
        response = self.request.send(url=url, method=method, headers=headers, json=data)
        res = response.json()
        # 对预期结果和相应结果进行断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
        except AssertionError as E:
            self.excel.write_data(row=row, column=8, value='不通过')
            log.error('{}用例不通过'.format(case['title']))
            log.exception(E)
            raise E
        else:
            self.excel.write_data(row=row, column=8, value='通过')
