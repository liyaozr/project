"""
============================
Author:柠檬班-木森
Time:2020/2/19   20:02
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import requests

# url = "https://www.baidu.com/"
#
#
# # 发送请求
# response = requests.get(url=url)
#
# # 获取服务器返回的内容
# # 方式一：text属性：自动识别返回内容的编码方式，进行解码（有可能会出现乱码）
# # print(response.text)
# # 方式二：content属性:需要使用decode方法，指定编码方式进行解码
# print(response.content.decode("utf8"))

# 方式三：json()方法：只要服务器返回的数据是json类型的时候，才可以使用该方法


# 发送请求的时候加上请求头
url = "https://www.baidu.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
}

response = requests.get(url=url,headers=headers)
# print(response.content.decode("utf8"))


print(response.headers)