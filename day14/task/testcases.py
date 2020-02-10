"""
============================
Author:luli
time:2020/1/24
company:happy
============================
"""
import unittest
from day14.task.login import login_check


class LoginTest(unittest.TestCase):
    def __init__(self, method, data):
        self.data = data
        super().__init__(method)

    def test_login(self):
        data = self.data['data']
        excepted = self.data['excepted']
        res = login_check(*data)
        self.assertEqual(excepted, res)
