"""
============================
Author:柠檬班-木森
Time:2020/2/19   21:13
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import requests

# url = "https://www.xfz.cn/api/website/articles/?p=2&n=20&type="
# # res = requests.get(url=url)
# #
# # print(res.json())

url = "https://www.xfz.cn/api/website/articles/"

data = {
    "p": 2,
    "n": 20
}
# params用来传递查询字符串参数，常用于get请求传递参数
res = requests.get(url=url,params=data)

print(res.json())