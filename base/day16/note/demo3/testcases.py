"""
============================
Author:柠檬班-木森
Time:2020/2/10   20:35
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from py26_16day.demo3.login import login_check
from py26_16day.demo3.ddt import ddt, data
from py26_16day.demo3.readexcel import ReadExcel


@ddt
class LoginTestCase(unittest.TestCase):
    excel = ReadExcel("cases.xlsx", "login")
    cases = excel.read_data()

    # [{},{},{},{}]
    @data(*cases)
    def test_login(self, case):
        """注册用例"""
        print("这个是接收到的case:", case)
        # 第一步：准备用例数据
        # 入参
        data = eval(case["data"])
        # 预期结果
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        # 第二步：获取实际结果
        # 实际结果(传入参数，调用待测试的功能函数)
        res = login_check(*data)

        # 第三步：比较预期结果和实际结果（断言）
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            # 在excel中写入用例未通过
            self.excel.write_data(row=row, column=5, value="未通过")
            raise e
        else:
            # 在excel中写入用例通过
            self.excel.write_data(row=row, column=5, value="通过")

    # @data(1111,222,33,44,555) # 根据参数生成测试用例（传几个参数就生成几条用例）
    # def test_login(self, case_data):
    #     print("这个是接收到的case:", case_data)
    #     # 第一步：准备用例数据
    #     # 入参
    #     data = eval(case_data["data"])
    #     # 预期结果
    #     expected = eval(case_data["expected"])
    #
    #     # 第二步：获取实际结果
    #     # 实际结果(传入参数，调用待测试的功能函数)
    #     res = login_check(*data)
    #
    #     # 第三步：比较预期结果和实际结果（断言）
    #     self.assertEqual(expected, res)
