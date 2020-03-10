"""
============================
Author:luli
Time:2020/3/9
Company:Happy
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
from common.handledata import CaseData, replace_data

case_file = os.path.join(DATADIR, 'apicases.xlsx')


@ddt
class TestMain(unittest.TestCase):
    excel = ReadExcel(case_file, 'mainflow')
    datas = excel.read_data()
    request = SendRequest()

    @data(*datas)
    def test_main(self, case):
        # 准备数据
        url = conf.get('env', 'url') + case['url']
        method = case['method']
        headers = eval(conf.get('env', 'headers'))
        if case['interface'] != 'login':
            headers['Api-User'] = getattr(CaseData, 'user')
            headers['Api-User-Token'] = getattr(CaseData, 'token')
        # 替换数据
        case['data'] = replace_data(case['data'])
        data = eval(case['data'])
        expected = eval(case['expected'])
        row = case['case_id'] + 1
        # 获取结果
        response = self.request.send(url=url, method=method, headers=headers, data=data)
        res = response.json()
        # 判断登录接口，获取信息
        if case['interface'] == 'login':
            CaseData.user = str(jsonpath.jsonpath(res, '$..user')[0])
            CaseData.token = str(jsonpath.jsonpath(res, '$..token')[0])
        if 'search' in case['interface']:
            CaseData.sku_id = str(jsonpath.jsonpath(res, '$..sku_id')[0])
            print('sku_id：', CaseData.sku_id)
        # 对预期结果和相应结果进行断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
        except AssertionError as E:
            print('user：', CaseData.user)
            print('token：', CaseData.token)

            print('预期结果：', expected['msg'])
            print('实际结果：', res['msg'])
            self.excel.write_data(row=row, column=8, value='不通过')
            log.error('{}用例不通过'.format(case['title']))
            log.exception(E)
            raise E
        else:
            self.excel.write_data(row=row, column=8, value='通过')
