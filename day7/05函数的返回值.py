"""
============================
Author:柠檬班-木森
Time:2020/1/8   21:30
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
函数的返回值
关键字：return
函数调用之后返回值是由return来决定的
函数没写return,函数返回的内容为None(为空)
return后面写什么，函数返回的就是什么


注意点：一个函数中只会执行一个return,函数执行到return之后就不会再继续执行，会直接跳出函数,返回结果
       函数可不可以写多个return？ 可以写多个，但是注意一个分支下只能写一个
问题：函数如何返回多个值？
    直接写在reurn后面，用逗号隔开
    返回两个及以上的值，会被放到元组中
       

"""

# def func11():
#     n = 10
#     print("这个是函数func11")
#     if 8 > n:
#         return "python888"
#     else:
#         print("------44------")
#         print("------555------")
#         return "999999"


# res = func11()
# print('-----res------', res)


#  字符串的split方法  :有返回值
# s = "456789"
# res2 = s.split("6")
# print('-----res2------',res2)


# 列表的append方法  ：没有返回值
# li = [1,2,3]
# res3 = li.append("999")
# print('-----res3------',res3)


# 函数返回多个值

def func222():
    return 111,222,4444


# res6 = func222()
# print("res6----",res6)

# 拆包，用多个变量接收多个值
a, b, c = func222()
print(a)
print(b)
print(c)