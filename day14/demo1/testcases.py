"""
============================
Author:luli
time:2020/1/24
company:happy
============================
"""

import unittest
from day14.demo1.register import register


class RegisterTest(unittest.TestCase):
    def __init__(self, methodName, data, expected):
        self.data = data
        self.expected = expected
        super().__init__(methodName)

    def test_register_success(self):
        data = self.data
        res = register(*data)
        self.assertEqual(self.expected, res)
