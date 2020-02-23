"""
============================
Author:luli
time:2020/2/23
company:happy
============================
"""
import os
import unittest
import random
from library.ddt import ddt, data
from common.readexcel import ReadExcel
from common.handlepath import DATADIR
from common.handlerequest import SendRequest
from common.handleconf import conf
from common.handlelog import log

case_file = os.path.join(DATADIR, 'apicases.xlsx')


@ddt
class TestRegister(unittest.TestCase):
    excel = ReadExcel(case_file, 'register')
    datas = excel.read_data()
    request = SendRequest()

    @data(*datas)
    def test_regiter(self, case):
        # 准备测试数据
        url = conf.get('env', 'url') + case['url']
        method = case['method']
        headers = eval(conf.get('env', 'headers'))
        phone = self.random_phone()
        case['data'] = case['data'].replace('#phone#', phone)
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

    def random_phone(self):
        random_num = ''.join(random.sample('0123456789', 8))
        phone = '130' + random_num
        return phone
