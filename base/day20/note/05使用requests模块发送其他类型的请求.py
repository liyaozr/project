"""
============================
Author:柠檬班-木森
Time:2020/2/19   21:20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
patch请求
"""

import requests

url = "http://api.lemonban.com/futureloan/member/update"

headers = {
    "X-Lemonban-Media-Type": "lemonban.v1"
}

data = {
    "member_id": "9579404",
    "reg_name": "python6"
}

res = requests.patch(url=url, json=data, headers=headers)

print(res.json())
