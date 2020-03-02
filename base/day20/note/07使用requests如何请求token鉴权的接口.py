"""
============================
Author:柠檬班-木森
Time:2020/2/19   21:27
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import requests

#
# # 请求头
# headers = {
#     "X-Lemonban-Media-Type": "lemonban.v2"
# }
# # 登录的请求
# url = "http://api.lemonban.com/futureloan/member/login"
# data = {
#     "mobile_phone": "13367899876",
#     "pwd": "lemonban"
# }
# res = requests.post(url=url, json=data, headers=headers)
# print(res.json())
#
# # 充值的请求
# print('-------------------充值--------------------------')
# re_url = "http://api.lemonban.com/futureloan/member/recharge"
# re_data = {
#     "member_id": 74711,
#     "amount": 2000
# }
# res = requests.post(url=re_url, json=re_data, headers=headers)
# print(res.json())

# ----------------------上面方式无法通过鉴权，下面是正确的操作方法--------------------------------------------

headers = {
    "X-Lemonban-Media-Type": "lemonban.v2"
}
# 登录的请求
url = "http://api.lemonban.com/futureloan/member/login"
data = {
    "mobile_phone": "13367899876",
    "pwd": "lemonban"
}
res = requests.post(url=url, json=data, headers=headers)
# 重登录返回的数据中，提取token
data = res.json()
token = data["data"]["token_info"]["token"]
token_type = data["data"]["token_info"]["token_type"]

token_value = token_type + " " + token

# 在请求头中添加token
headers["Authorization"] = token_value

# 充值的请求
print('-------------------充值--------------------------')
re_url = "http://api.lemonban.com/futureloan/member/recharge"
re_data = {
    "member_id": 74711,
    "amount": 2000
}
res2 = requests.post(url=re_url, json=re_data, headers=headers)
print(res2.json())
