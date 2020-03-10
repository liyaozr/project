"""
============================
Author:luli
Time:2020/3/6
Company:Happy
============================
"""

import smtplib
from email.mime.text import MIMEText

'''
smtp服务器：
smtp服务器地址：
qq邮箱：smtp.qq.com   端口：465
163邮箱：smtp.163.com  端口：465
账号：3232069481@qq.com 
授权码：nfmjpitohvfecgji
'''

smtp = smtplib.SMTP_SSL(host='smtp.qq.com', port=465)
smtp.login(user='3232069481@qq.com', password='nfmjpitohvfecgji')
# 1、发送普通内容

# content = '这是使用python发的第一封邮件'
# msg = MIMEText(content, _subtype='plain', _charset='utf8')
# msg['Subject'] = '26期上课发送邮件'
# msg['From'] = '3232069481@qq.com'
# msg['To'] = '597933791@qq.com'

# 2、发送附件
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

msg = MIMEMultipart()
with open('report.html', 'rb')as f:
    content = f.read()

text_msg = MIMEText(content, _subtype='html', _charset='utf8')
msg.attach(text_msg)
report_file = MIMEApplication(content)
report_file.add_header('content-disposition', 'attachment', filename='26report.html')
msg.attach(report_file)

msg['Subject'] = '26期上课发送邮件'
msg['From'] = '3232069481@qq.com'
msg['To'] = '597933791@qq.com'
smtp.send_message(msg, from_addr='3232069481@qq.com', to_addrs='597933791@qq.com')
