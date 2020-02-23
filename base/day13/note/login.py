"""
============================
Author:柠檬班-木森
Time:2019/11/15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


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





# 第一条用例
# 入参：账号python26  密码lemonban
# 预期结果：{"code": 0, "msg": "登录成功"}
expected = {"code": 0, "msg": "登录成功"}
# # 实际结果：
res = login_check('python26', "lemonban")
# 判断预期结果是否等于实际结果
if expected == res:
    print("用例执行通过")
else:
    print("用例执行不通过该")


# 断言 assert 条件语句
"""
断言条件不通过，会报错（断言异常）
断言条件通过，不会有任何返回，直接执行下一行代码
"""

# assert expected == "7890"
#
# print("断言通过")


