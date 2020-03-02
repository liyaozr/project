"""
============================
Author:柠檬班-木森
Time:2020/1/17   21:14
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
类可以用来封装属性和方法：

属性：定义在类里面的变量

类属性：直接定义在类里面的变量(这个类的每个对象都有这个属性，而且属性值是一样的)
    类属性的定义：直接定义在类里面的变量
    
对象属性（实例属性）：这一类事物都可能会有这个属性，属性值有可能不一样
    对象属性的定义：
        方式一：通过对象进行赋值:  对象.属性 = 属性值
        方式二：通过初始化方法__init__进行定义:self.属性 = 属性值
                

方法：定义在类里的函数

对象：通过类创建出来的，拥有这个类所以的特征和行为

通过类创建对象：
    obj = 类名（）


self:代表的是对象本身，那个对象去调用方法，self代表的就是那个对象


"""


# 名字、年龄、性别


class Cat:
    attr1 = "喵喵喵"
    attr2 = "长毛"
    attr3 = "爱吃鱼"
    attr4 = "爱睡觉"


# 创建对象
# c1 = Cat()
# # 用过对象添加属性
# c1.name = "叮当猫"
# c1.gender = "公"
# c1.age = 18
#
#
# c2 = Cat()
# c2.name = "凯蒂猫"
# c2.gender = "母"
# c2.age = 16
#
#
# c3 = Cat()
# c3.name = "机器猫"
# c3.gender = "中性"
# c3.age = 1


# print(c1.attr1)
# print(c2.attr1)
# print(id(c1))
# print(id(c2))


# -------------------------初始化方法__init__:--------------------------------

class Cat:
    attr1 = "喵喵喵"
    attr2 = "长毛"
    attr3 = "爱吃鱼"
    attr4 = "爱睡觉"

    def __init__(self, name, gender, age):
        # 通过类去创建对象的时候，该方法会自动调用
        # 初始化对象属性
        print("这个是self:",self)
        print(name,gender,age)
        self.name = name
        self.age = age
        self.gender = gender
        print("init方法创建对象的时候自动调用了")


c1 = Cat("叮当猫", "公猫", 18)
print("这个是c1",c1)


c2 = Cat("机器猫","母猫",1)
print("这个是c2",c2)


# def fun():
#     pass
#
# print(fun)








