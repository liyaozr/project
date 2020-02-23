"""
============================
Author:柠檬班-木森
Time:2020/1/15   21:57
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
try：
    # 有可能会出现异常
except:
    #




# 下次课内容：
捕获指定异常类型

同时捕获多个异常类型，采取不同的方法处理


# 面向的使用
什么是类？
什么是对象？
类的定义？
类属性 
方法

"""
# 打开文件的时候，文件有可能会不存在
try:
    with open("yyyy.txt", "r") as f:
        c = f.read()
except:
    print("代码出现了异常")

else:
    print("代码没有报错")

# 用户输入的数据没办法控制，有可能会出现异常
try:
    with open("yyyy.txt", "r") as f:
        c = f.read()
    num = int(input("请输入一个数字："))
except:
    print("你输入的不符合规范")
else:
    if num > 5:
        print("数字大于5")


# 发送网络请求