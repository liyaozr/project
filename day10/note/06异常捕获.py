"""
============================
Author:柠檬班-木森
Time:2020/1/15   21:45
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
try: 监测有可能出现异常的代码
except:捕获异常，对异常进行处理
else:没有发送异常，的处理方式，放在else中
finally:不管代码是否发送异常都会执行


try:
    # try下面方有可能会出现异常的代码
except:
    # except下面放捕获到异常之后处理的代码
else:
    # else：没有出现异常，会执行else中的代码
finally:
    # finally 不管代码是否发送异常都会执行
"""
try:
    with open("yyyy11.txt", "r")as f:
        content = f.read()
except:
    print("except:------捕获到异常之后的处理方式")
    with open("yyyy.txt", "w")as f:
        pass
else:
    print("esle:-------代码没有出现异常处理的方式，可以写在这里")
    print(content)
finally:
    print("finally:-------不管代码是否出现异常都会执行")


print("---------1----------")
print("---------2----------")
