"""
============================
Author:柠檬班-木森
Time:2020/2/19   21:52
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import requests
import jsonpath

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

data = res.json()
# print(data)
# 提取token
token = jsonpath.jsonpath(data, "$..token")[0]
print(token)
# 提取token值
token_type = jsonpath.jsonpath(data, "$..token_type")[0]
print(token_type)
# 提取reg_name
reg_name = jsonpath.jsonpath(data, "$..reg_name")[0]
print(reg_name)


