"""
============================
Author:柠檬班-木森
Time:2020/1/3   21:22
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
if  条件1：
    # 条件1成立执行的代码
elif 条件2：
    # 条件3成立执行的代码
elif 条件3：
    # 条件3成立执行的代码
else:
    # 以上条件都不成立执行的代码
    
# 开启一个条件判断：使用if
elif:在条件判断语句中可以不写，也可以写一个或者多个（根据需求来）
else:在条件判断语句中可以不写,也可以写一个(根据需求) 

    

"""

# 需求一：用户输入考试成绩，请判断是否及格？
num = int(input("请输入成绩："))
# 单独使用一个if
if num >= 60:
    print("考试及格")

# 需求二：完善需求一，当用户输入成绩不及格时，打印 考试不及格，晚上通宵敲代码！
# if结合else一起使用
if num >= 60:
    print("考试及格")
else:
    print("考试不及格，代码敲通宵")

# 需求三：对考试成绩进行分等级，60-69:及格，70-79：良好，80-89：优秀，90-100：顶呱呱，60以下不及格

if 60 <= num <= 69:
    print("及格")
elif 70 <= num <= 79:
    print("良好")
elif 80 <= num <= 89:
    print("优秀")
elif 90 <= num <= 100:
    print("顶呱呱")
elif 0 <= num < 60:
    print("不及格")
else:
    print("您输入的成绩不规范")

# 优化判断的区间，通过判断的流程来控制条件的区间
# if 0 <= num < 60:
#     print("不及格")
# elif num < 70:
#     print("及格")
# elif num < 80:
#     print("良好")
# elif num < 90:
#     print("优秀")
# elif num <= 100:
#     print("顶呱呱")
# else:
#     print("您输入的成绩不规范")


#  条件语句的嵌套使用

"""
需求一：如果是账号不对：打印输入的账号有误
需求二：如果是密码不对：打印输入的密码有误
需求三：如果账号密码都正确，打印登录成功


"""
# user = "py26"
# pwd = "lemonban"

# username = input('请输入账号：')
# password = input("请输入密码：")

# if user == username:
#     if pwd == password:
#         print("登录成功")
#     else:
#         print("输入的密码有误")
# else:
#     print("输入的账号有误")


"""
需求1：如果是账号或密码不对：打印输入的账号或密码有误
需求2：如果账号密码都正确，打印登录成功

"""

# 添加判断结合逻辑运算符一起使用
# and:一假即假
# or：一真为真
# not

# if user == username and pwd == password:
#     print("登录成功")
# else:
#     print('输入的账号或密码有误')


# if 判断成不成立：取决于后面表达式的布尔值是否为True，为True成立，否则不成立

# 扩展：python中数据的布尔值
# python中的任何数据都有布尔值，通过bool这个函数可以获取数据的布尔值
# python中数据的布尔值: 非0为True
                # 0的含义：数字0布尔值 为False
                # 数据的长度为0布尔值 为False
                # None的布尔值 为False
print(bool())

if True:
    print("成立")







