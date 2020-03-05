"""
============================
Author:luli
time:2020/2/26
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
from decimal import Decimal
from common.handledata import CaseData, replace_data
from common.handle_sign import HandleSign

case_file = os.path.join(DATADIR, 'apicases.xlsx')


@ddt
class TestWithdraw(unittest.TestCase):
    excel = ReadExcel(case_file, 'withdraw')
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
        headers = {"X-Lemonban-Media-Type": "lemonban.v3"}
        response = cls.request.send(url=url, method=method, headers=headers, json=data)
        res = response.json()
        token = jsonpath.jsonpath(res, "$..token")[0]
        # CaseData.token = token
        token_type = jsonpath.jsonpath(res, "$..token_type")[0]
        CaseData.token_value = token_type + " " + token
        CaseData.member_id = str(jsonpath.jsonpath(res, "$..id")[0])
        CaseData.sign = HandleSign.generate_sign(token)

    @data(*datas)
    def test_withdaw(self, case):
        # 准备数据
        url = conf.get('env', 'url') + case['url']
        method = case['method']
        headers = eval(conf.get('env', 'headers'))
        # 请求头中添加token
        headers['Authorization'] = getattr(CaseData, 'token_value')
        # 替换测试数据
        case['data'] = replace_data(case['data'])
        data = eval(case['data'])
        data.update(CaseData.sign)
        print(data)
        expected = eval(case['expected'])
        row = case['case_id'] + 1
        # 发送请求之前,获取用余额
        if case['check_sql']:
            sql = 'SELECT leave_amount FROM futureloan.member WHERE mobile_phone={}'.format(
                conf.get('test_data', 'phone'))
            # 查询当前用户的余额
            start_money = self.db.find_one(sql)['leave_amount']
        # 获取结果
        response = self.request.send(url=url, method=method, headers=headers, json=data)
        res = response.json()
        # 对预期结果和相应结果进行断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
            # 判断示范需要进行sql校验
            if case['check_sql']:
                sql = 'SELECT leave_amount FROM futureloan.member WHERE mobile_phone={}'.format(
                    conf.get('test_data', 'phone'))
                # 查询当前用户的余额
                end_money = self.db.find_one(sql)['leave_amount']
                self.assertEqual(start_money - end_money, Decimal(str(data['amount'])))
        except AssertionError as E:
            print('预期结果：', expected['msg'])
            print('实际结果：', res['msg'])
            self.excel.write_data(row=row, column=8, value='不通过')
            log.error('{}用例不通过'.format(case['title']))
            log.exception(E)
            raise E
        else:
            self.excel.write_data(row=row, column=8, value='通过')
