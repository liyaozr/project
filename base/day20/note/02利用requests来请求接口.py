"""
============================
Author:柠檬班-木森
Time:2020/2/19   20:22
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import requests

# 注册的接口地址：
# url = "http://api.lemonban.com/futureloan/member/register"
url = "http://httpbin.org/post"
# 请求头
headers = {
    "X-Lemonban-Media-Type": "lemonban.v1"
}
# 请求参数
data = {
    "mobile_phone":"15798765678",
    "pwd":"lemonban",
    "type":1,
    "reg_name":"木森"
}


# 发送请求
# 1、json类型的参数
# 参数使用json传递的时候会自动加上请求头，Content-type:"application/json"
# response = requests.post(url=url,headers=headers,json=data)
#
# # 2、表单类型的参数：Content-Type:"application/x-www-form-urlencoded"
# # 参数使用data传递的时候会自动加上请求头，Content-type:application/x-www-form-urlencoded
# response = requests.post(url=url,data=data)
#
# # 3、"multipart/form-data参数：一般用于上传文件
# # 参数使用files传递的时候会自动加上请求头，Content-Type": "multipart/form-data; boundary=5bf6afd23971d662cf5a2d9aa2f585e9"
# file_data = {"file1":("01reuqests.py",open("01requests发送网络请求.py","rb"),"text/py")}
# response = requests.post(url=url, files=file_data)


# 打印接口返回的内容
print(response.text)

