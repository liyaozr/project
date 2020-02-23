"""
============================
Author:柠檬班-木森
Time:2020/2/19   21:27
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import requests

# 使用cookie+session鉴权
# 使用requests中的session对象来发送请求
# 使用session对象先登录，登录之后session对象会自动记录cookie信息，在请求需要登录的接口就可以通过鉴权
s = requests.session()

# 老版本的前程贷登录
url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
data = {
    "mobilephone": "13367899876",
    "pwd": "lemonban"
}
res = s.post(url=url, data=data)
print(res.json())

# 充值接口
re_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
re_data = {
    "amount": 2000,
    "mobilephone": "13367899876"

}
res2 = s.post(url=re_url, data=re_data)
print(res2.json())


#  -------失败案例：使用request直接请求，无法通过鉴权
# 老版本的前程贷登录
# url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
# data = {
#     "mobilephone": "13367899876",
#     "pwd": "lemonban"
# }
# res = requests.post(url=url, data=data)
# print(res.json())
#
# # 充值接口
# re_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
# re_data = {
#     "amount": 2000,
#     "mobilephone": "13367899876"
#
# }
# res2 = requests.post(url=re_url, data=re_data)
# print(res2.json())