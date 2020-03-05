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

'''
投资接口：
1、需要有标：管理员登录，加标、审核，
2、用户登录
3、投资用例的执行

# 关于投资的sql校验语句
1、用户表、校验用户余额是否发生变化，变化金额等于所投金额（根据用户id去查member表）
2、根据用户id和标id去投资表中查用户的投资记录，（invest里面查用户对应的标是否新增一条记录）
3、根据用户id去流水标中查询流水记录（查询用户投资之后是否多了一条记录）
4、在刚好投满的情况下，可以根据投资记录的id，去回款计划表中查询是否，生成回款计划。
'''
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
        # 保存token
        CaseData.token_value = token_type + ' ' + token
        # 保存用户id
        CaseData.member_id = str(jsonpath.jsonpath(res, '$..id')[0])
        # 保存用户初始金额
        CaseData.start_user_amount = jsonpath.jsonpath(res, '$..leave_amount')[0]

    def setUp(self):
        # 在竞标状态的项目id
        sql = 'SELECT id FROM  futureloan.loan WHERE status = 2'
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
            sql1 = 'SELECT amount FROM futureloan.loan WHERE id={};'.format(CaseData.loan_id)
            project_amount = self.db.find_one(sql1)['amount']
            sql2 = 'SELECT sum(amount) FROM futureloan.invest WHERE loan_id={};'.format(CaseData.loan_id)
            invest_amount = self.db.find_one(sql2)['sum(amount)'] or 0
            CaseData.project_amount = str(project_amount - invest_amount)

            # 查询用户的初始投标数量
            sql_invest = 'SELECT count(member_id) FROM futureloan.invest WHERE member_id={} and loan_id={}'.format(
                CaseData.member_id, CaseData.loan_id)
            start_invest_num = self.db.find_one(sql_invest)['count(member_id)']

            # 查询用户的初始流水记录
            sql_finance = 'SELECT count(pay_member_id) FROM futureloan.financelog WHERE pay_member_id={}'.format(
                CaseData.member_id)
            start_finance = self.db.find_one(sql_finance)['count(pay_member_id)']
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
            # 对预期结果和响应结果进行断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
            if case['check_sql'] == 1:
                # 1、用户表、校验用户余额是否发生变化，变化金额等于所投金额（根据用户id去查member表）
                sql_amonut = 'SELECT leave_amount FROM futureloan.member WHERE id={}'.format(CaseData.member_id)
                end_user_amount = self.db.find_one(sql_amonut)['leave_amount']
                self.assertEqual(Decimal(str(CaseData.start_user_amount)) - end_user_amount,
                                 Decimal(str(data['amount'])))
                # 2、根据用户id和标id去投资表中查用户的投资记录，（invest里面查用户对应的标是否新增一条记录）
                end_invest_num = self.db.find_one(sql_invest)['count(member_id)']
                self.assertEqual(end_invest_num - start_invest_num, 1)
                # 3、根据用户id去流水标中查询流水记录（查询用户投资之后是否多了一条记录）
                end_finance = self.db.find_one(sql_finance)['count(pay_member_id)']
                self.assertEqual(end_finance - start_finance, 1)
            # 4、在刚好投满的情况下，可以根据投资记录的id，去回款计划表中查询是否，生成回款计划。
            if case['check_sql'] == 4:
                invest_id = jsonpath.jsonpath(res, '$..id')[0]
                sql_repayment = 'SELECT invest_id FROM futureloan.repayment WHERE id={}'.format(invest_id)
                repayment = self.db.find_one(sql_repayment)['invest_id']
                self.assertTrue(repayment)

        except AssertionError as E:
            print('预期结果：', expected)
            print('实际结果：', res)
            self.excel.write_data(row=row, column=8, value='不通过')
            log.error('{}用例不通过'.format(case['title']))
            log.exception(E)
            raise E
        else:
            self.excel.write_data(row=row, column=8, value='通过')
