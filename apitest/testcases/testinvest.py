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
from decimal import Decimal
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
class TestInvest(unittest.TestCase):
    excel = ReadExcel(case_file, 'invest')
    datas = excel.read_data()
    request = SendRequest()
    db = DB()

    @classmethod
    def setUpClass(cls):
        """登陆"""
        data = {
            'mobile_phone': conf.get('test_data', 'phone'),
            'pwd': conf.get('test_data', 'pwd')
        }
        url = conf.get('env', 'url') + '/member/login'
        headers = eval(conf.get('env', 'headers'))
        response = cls.request.send(url=url, method='post', headers=headers, json=data)
        res = response.json()
        token = jsonpath.jsonpath(res, '$..token')[0]
        token_type = jsonpath.jsonpath(res, '$..token_type')[0]
        CaseData.token_value = token_type + ' ' + token
        CaseData.member_id = str(jsonpath.jsonpath(res, '$..id')[0])
        CaseData.user_amount = str((jsonpath.jsonpath(res, '$..leave_amount')[0] // 100 * 100) + 500)

    def setUp(self):
        # 在竞标状态的项目id
        sql = 'SELECT id FROM  futureloan.loan WHERE status = 2 and 1000<amount<10000;'
        CaseData.loan_id = str(self.db.find_one(sql)['id'])
        # 不在竞标状态的项目id
        sql = 'SELECT id FROM  futureloan.loan WHERE status = 5;'
        CaseData.fail_loan_id = str(self.db.find_one(sql)['id'])

    @data(*datas)
    def test_invest(self, case):
        # 准备数据
        url = conf.get('env', 'url') + case['url']
        method = case['method']
        headers = eval(conf.get('env', 'headers'))
        headers['Authorization'] = getattr(CaseData, 'token_value')
        if case['check_sql']:
            # 查询项目的剩余竞标金额
            sql1 = 'SELECT amount FROM  futureloan.loan WHERE id={};'.format(CaseData.loan_id)
            project_amount = self.db.find_one(sql1)['amount']
            sql2 = 'SELECT sum(amount) FROM  futureloan.invest WHERE loan_id={};'.format(CaseData.loan_id)
            invest_amount = self.db.find_one(sql2)['sum(amount)']
            # 将剩余的竞标金额+100，来测试投资金额大于项目可投余额
            CaseData.project_amount = str(project_amount - invest_amount + Decimal('100'))
        case['data'] = replace_data(case['data'])
        data = eval(case['data'])
        expected = eval(case['expected'])
        row = case['case_id'] + 1
        # 获取结果
        response = self.request.send(url=url, method=method, headers=headers, json=data)
        res = response.json()
        if case['check_sql'] == 2:
            invest_amount = self.db.find_one(sql2)['sum(amount)']
            CaseData.leave_amount = str(round(project_amount - invest_amount, 1))
            expected = eval(replace_data(case['expected']))
        # 对预期结果和相应结果进行断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
            if case['check_sql'] == 1:
                self.assertEqual(Decimal(str(data['amount'])), Decimal(str(res['data']['amount'])))
        except AssertionError as E:
            print(case['check_sql'])
            print('预期结果：', expected)
            print('实际结果：', res)
            self.excel.write_data(row=row, column=8, value='不通过')
            log.error('{}用例不通过'.format(case['title']))
            log.exception(E)
            raise E
        else:
            self.excel.write_data(row=row, column=8, value='通过')
