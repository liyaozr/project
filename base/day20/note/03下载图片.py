"""
============================
Author:柠檬班-木森
Time:2020/2/19   21:04
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import requests

url = "https://www.baidu.com/img/bd_logo1.png"



response = requests.get(url=url)

with open("baidu.png","wb") as f:
    f.write(response.content)

