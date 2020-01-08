"""
============================
Author:柠檬班-木森
Time:2020/1/8   20:36
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
请设计一段程序输出，下面的内容：
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5  

# 设计一个程序输出 一个乘法口诀表：
 
"""

# for i in range(1, 6):
#     print()
#     for j in range(1, i + 1):
#         print('{} '.format(j), end="")

#  列表推导式（扩展知识点：课纲之外的）
#  需求：  快速生成一个 ["page1","page2","page3","page4"]
li = []

for i in range(1, 5):
    num = "page{}".format(i)
    li.append(num)

print(li)

# 列表推导式（帮我们快速生成列表）
li1 = ["page{}".format(i) for i in range(1, 5)]
print(li1)






# 字典推导式（测开内容）









