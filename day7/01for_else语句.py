"""
============================
Author:柠檬班-木森
Time:2020/1/8   20:18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
for_else语句：for循环遍历结束之后会执行else,如果使用break跳出循环，则不会执行



注册小案例：
users = [{"user":"py1","pwd":"123"},{"user":"py2","pwd":"111"}]
需求：设计一个注册程序，注册的时候，提示用户输入账号密码，输入完了之后，
校验该账号之前是否已经注册过，如果没有注册过，则添加到users中保存，
如果注册过了，提示该用户已经注册

难点：如何去判断用户有没有注册过？



"""
# for  else语句
# li = [1, 2, 3, 4, 5]
#
# for i in li:
#     print(i)
#     # if i == 3:
#     #     break
# else:
#     print("for循环遍历结束之后会执行else,如果使用break跳出循环，则不会执行")
#
# print("程序运行结束")


# 小案例
users = [{"user": "py1", "pwd": "123"}, {"user": "py2", "pwd": "111"}]

name = input("请输入账号：")
pwd = input("输入密码：")

# 判断账户是否已经注册？
for item in users:
    if name == item["user"]:
        print("该用户已经注册")
        break
else:
    print("注册成功")
    # 把账号密码添加到 users中
    users.append({"user": name, "pwd": pwd})