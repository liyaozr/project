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
from common.connectdb import DB
from common.handledata import CaseData, replace_data

case_file = os.path.join(DATADIR, 'apicases.xlsx')


@ddt
class TestInfo(unittest.TestCase):
    excel = ReadExcel(case_file, 'info')
    datas = excel.read_data()
    request = SendRequest()
    db = DB()

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
        CaseData.member_id = str(jsonpath.jsonpath(res, "$..id")[0])

    @data(*datas)
    def test_info(self, case):
        # 准备数据
        url = conf.get('env', 'url') + replace_data(case['url'])
        method = case['method']
        headers = eval(conf.get('env', 'headers'))
        headers['Authorization'] = getattr(CaseData, 'token_value')
        expected = eval(case['expected'])
        row = case['case_id'] + 1

        # 获取结果
        response = self.request.send(url=url, method=method, headers=headers)
        res = response.json()

        # 对预期结果和响应结果进行断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertIn(expected['msg'], res['msg'])
            # 对获取信息成功的用例进行数据库校验
            if case['check_sql']:
                sql = 'SELECT mobile_phone FROM  futureloan.member WHERE id={};'.format(CaseData.member_id)
                mobile_phone = self.db.find_one(sql)['mobile_phone']
                self.assertEqual(jsonpath.jsonpath(res, "$..mobile_phone")[0], mobile_phone)

        except AssertionError as E:
            print('预期结果：', expected['msg'])
            print('实际结果：', res['msg'])
            self.excel.write_data(row=row, column=7, value='不通过')
            log.error('{}用例不通过'.format(case['title']))
            log.exception(E)
            raise E
        else:
            self.excel.write_data(row=row, column=7, value='通过')
