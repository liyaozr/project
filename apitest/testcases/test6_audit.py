"""
============================
Author:luli
time:2020/3/1
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
from common.connectdb import DB
from common.handledata import CaseData, replace_data

case_file = os.path.join(DATADIR, 'apicases.xlsx')


@ddt
class TestAudit(unittest.TestCase):
    excel = ReadExcel(case_file, 'audit')
    datas = excel.read_data()
    request = SendRequest()
    db = DB()

    @classmethod
    def setUpClass(cls):
        """使用管理员账号登陆"""
        data = {
            'mobile_phone': conf.get('test_data', 'admin_phone'),
            'pwd': conf.get('test_data', 'admin_pwd')
        }
        url = conf.get('env', 'url') + '/member/login'
        headers = eval(conf.get('env', 'headers'))
        response = cls.request.send(url=url, method='post', headers=headers, json=data)
        res = response.json()
        token = jsonpath.jsonpath(res, "$..token")[0]
        token_type = jsonpath.jsonpath(res, "$..token_type")[0]
        CaseData.admin_token_value = token_type + " " + token
        CaseData.admin_member_id = str(jsonpath.jsonpath(res, "$..id")[0])

    def setUp(self):
        url = conf.get('env', 'url') + '/loan/add'
        headers = eval(conf.get('env', 'headers'))
        headers['Authorization'] = getattr(CaseData, 'admin_token_value')
        data = eval(conf.get('test_data', 'add_data'))
        data['member_id'] = getattr(CaseData, 'admin_member_id')
        response = self.request.send(url=url, method='post', headers=headers, json=data)
        self.add_res = response.json()
        # 保存新增的项目id
        CaseData.loan_id = str(jsonpath.jsonpath(self.add_res, "$..id")[0])

    @data(*datas)
    def test_audit(self, case):
        # 准备数据
        url = conf.get('env', 'url') + case['url']
        method = case['method']
        headers = eval(conf.get('env', 'headers'))
        headers['Authorization'] = getattr(CaseData, 'admin_token_value')
        case['data'] = replace_data(case['data'])
        data = eval(case['data'])
        expected = eval(case['expected'])
        row = case['case_id'] + 1

        # 获取结果
        response = self.request.send(url=url, method=method, headers=headers, json=data)
        res = response.json()
        if case['check_sql']:
            sql = 'SELECT status FROM  futureloan.loan WHERE id={};'.format(CaseData.loan_id)
            status = self.db.find_one(sql)['status']
            # 保存审核通过的项目id
            if status == 2:
                CaseData.pass_loan_id = str(data['loan_id'])
        # 对预期结果和相应结果进行断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
            if case['check_sql']:
                self.assertEqual(expected['status'], status)
        except AssertionError as E:
            print('预期结果：', expected)
            print('实际结果：', res)
            self.excel.write_data(row=row, column=8, value='不通过')
            log.error('{}用例不通过'.format(case['title']))
            log.exception(E)
            raise E
        else:
            self.excel.write_data(row=row, column=8, value='通过')

    # def tearDown(self):
    #     sql = 'DELETE FROM futureloan.loan WHERE id={};'.format(CaseData.loan_id)
    #     self.db.delete_data(sql)
