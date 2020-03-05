"""
============================
Author:luli
time:2020/2/27
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
class TestAdd(unittest.TestCase):
    excel = ReadExcel(case_file, 'add')
    datas = excel.read_data()
    request = SendRequest()
    db = DB()

    @classmethod
    def setUpClass(cls):
        data = {
            'mobile_phone': conf.get('test_data', 'admin_phone'),
            'pwd': conf.get('test_data', 'admin_pwd')
        }
        url = conf.get('env', 'url') + '/member/login'
        method = 'post'
        headers = eval(conf.get('env', 'headers'))
        response = cls.request.send(url=url, method=method, headers=headers, json=data)
        res = response.json()
        token = jsonpath.jsonpath(res, "$..token")[0]
        token_type = jsonpath.jsonpath(res, "$..token_type")[0]
        CaseData.admin_token_value = token_type + " " + token
        CaseData.admin_member_id = str(jsonpath.jsonpath(res, "$..id")[0])

    @data(*datas)
    def test_add(self, case):
        # 准备数据
        url = conf.get('env', 'url') + case['url']
        method = case['method']
        headers = eval(conf.get('env', 'headers'))
        headers['Authorization'] = getattr(CaseData, 'admin_token_value')
        case['data'] = replace_data(case['data'])

        data = eval(case['data'])
        expected = eval(case['expected'])
        row = case['case_id'] + 1
        if case['check_sql']:
            sql = 'SELECT count(member_id) FROM futureloan.loan WHERE member_id={}'.format(
                CaseData.admin_member_id)
            start_res = self.db.find_one(sql)['count(member_id)']
        # 获取结果
        response = self.request.send(url=url, method=method, headers=headers, json=data)
        res = response.json()
        # 对预期结果和响应结果进行断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
            # 1、判断返回的项目id存不存在，如果不返回项目id，可以使用2、查询该member_id的项目有没有增加一个
            if case['check_sql']:
                sql = 'SELECT count(member_id) FROM futureloan.loan WHERE member_id={}'.format(
                    CaseData.admin_member_id)
                end_res = self.db.find_one(sql)['count(member_id)']
                self.assertEqual(end_res - start_res, 1)
        except AssertionError as E:
            print('预期结果：', expected)
            print('实际结果：', res)
            self.excel.write_data(row=row, column=8, value='不通过')
            log.error('{}用例不通过'.format(case['title']))
            log.exception(E)
            raise E
        else:
            self.excel.write_data(row=row, column=8, value='通过')
