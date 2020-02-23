"""
============================
Author:luli
time:2020/2/19
company:happy
============================
"""

import requests
import jsonpath

# 总链接
url = 'http://api.lemonban.com/futureloan'
# 初始头部信息
headers = {
    "X-Lemonban-Media-Type": "lemonban.v2"
}

# register----注册
register_url = url + '/member/register'

register_data = {
    'mobile_phone': '13058640005',
    'pwd': 'lemonban',
    'type': 1,
    'reg_name': '鹿梨'
}

register_response = requests.post(url=register_url, headers=headers, json=register_data)
print('-------------------------------------注册--------------------------------------------------')
print(register_response.json())

# login----登录
login_url = url + '/member/login'
# 这里的手机号要注册以后才能用，单独登录可以用13058640004
login_data = {
    'mobile_phone': '13058640005',
    'pwd': 'lemonban'
}

login_response = requests.post(url=login_url, headers=headers, json=login_data)

login_res = login_response.json()
print('-------------------------------------登录--------------------------------------------------')
print(login_res)

# recharge----充值
# 获取用户id
member_id = jsonpath.jsonpath(login_res, '$..id')[0]

# 获取token信息并且添加到头部
token_value = jsonpath.jsonpath(login_res, '$..token_type')[0] + ' ' + jsonpath.jsonpath(login_res, '$..token')[0]
headers['Authorization'] = token_value

recharge_url = url + '/member/recharge'
recharge_data = {
    'member_id': member_id,
    'amount': 1000
}

recharge_response = requests.post(url=recharge_url, headers=headers, json=recharge_data)

recharge_res = recharge_response.json()
print('-------------------------------------充值--------------------------------------------------')
print(recharge_res)

# withdraw----提现
withdraw_url = url + '/member/withdraw'

withdraw_data = {
    'member_id': member_id,
    'amount': 500
}

withdraw_response = requests.post(url=withdraw_url, headers=headers, json=withdraw_data)

withdraw_res = withdraw_response.json()
print('-------------------------------------提现--------------------------------------------------')
print(withdraw_res)
