"""
============================
Author:柠檬班-木森
Time:2020/1/6   21:11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""

# 利用while循环实现的登录小案例


"""

user_info = {"user": "python26", "pwd": "lemonban"}


while True:
    username = input("请输入账号：")
    password = input("请输入密码：")
    # 判断账号密码是否正确
    if username == user_info["user"] and password == user_info["pwd"]:
        print("登录成功")
        break
    else:
        print("账号或者密码有误")
