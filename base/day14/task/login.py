"""
============================
Author:luli
time:2020/1/24
company:happy
============================
"""
'''
将前面上课login_check这个功能函数的单元测试代码，进行代码和代码数据分离处理，用例数据保存在列表中
'''

def login_check(username=None, password=None):
    """
    登录校验的函数
    :param username: 账号
    :param password:  密码
    :return: dict type
    """
    if username != None and password != None:
        if username == 'python26' and password == 'lemonban':
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}
    else:
        return {"code": 1, "msg": "所以的参数不能为空"}