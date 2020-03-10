"""
============================
Author:luli
Time:2020/3/9
Company:Happy
============================
"""
from common.handlerequest import SendRequest
from common.handledata import CaseData
import jsonpath

request = SendRequest()
url = r'http://m.suyunweb.com/mobile/login/login'
headers = {'Api-AppId': 'xiangcheng', 'X-Requested-With': 'XMLHttpRequest'}
method = 'post'
data = {"mobile": "13065705608", "password": "jnHI4ryc=9bGmlei"}
response = request.send(url=url, method=method, headers=headers, data=data)
res = response.json()

CaseData.user = str(jsonpath.jsonpath(res, '$..user')[0])
CaseData.token = str(jsonpath.jsonpath(res, '$..token')[0])

url_index = r'http://m.suyunweb.com/mobile/index/new_index'
headers['Api-User'] = CaseData.user
headers['Api-User-Token'] = CaseData.token
response1 = request.send(url=url_index, method=method, headers=headers, data=data)
res1 = response1.json()
print(res1)
