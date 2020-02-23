"""
============================
Author:luli
time:2020/2/19
company:happy
============================
"""

import requests

# url = 'https://www.baidu.com'
#
# # 发送请求
# response = requests.get(url=url)
#
# # 获取服务器返回的内容
# # 方式一：text属性：自动识别返回内容的编码方式，进行编码（有可能会出现乱码）
# # print(response.text)
#
# print(response.content)


# 接口地址
url = 'http://api.lemonban.com/futureloan/member/register'
# 加请求头
headers = {'X-Lemonban-Media-Type': 'lemonban.v1'}
# 加请求参数
data = {
    'mobile_phone': '13058640000',
    'pwd': 'lemonban',
    'type': 1,
    'reg_name': 'luli'
}

# 发送请求
response = requests.post(url=url, headers=headers, json=data)
# 打印接口返回的内容
print(response.text)
