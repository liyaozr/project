"""
============================
Author:柠檬班-木森
Time:2020/1/13   21:22
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
with的使用
通过with打开文件，会自动帮我们关闭文件

with可以开启文件操作的上下文管理器


"""

with open("tttt.txt", "r", encoding="utf8") as f:
    content = f.read()
    print(content)
