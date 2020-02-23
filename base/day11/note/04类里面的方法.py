"""
============================
Author:柠檬班-木森
Time:2020/1/17   21:48
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
类里面的方法


方法（对象方法）：
类里面的定义的函数叫方法：
    方法的第一个参数必须写成self(这个规范)


self:代表的是对象本身，那个对象去调用方法，self代表的就是那个对象



# 下节课的内容：
静态方法：

类方法：



"""


class Cat:
    attr1 = "喵喵喵"
    attr2 = "长毛"
    attr3 = "爱吃鱼"
    attr4 = "爱睡觉"

    def __init__(self, name, gender, age):
        # 通过类去创建对象的时候，该方法会自动调用
        self.name = name
        self.age = age
        self.gender = gender

    def skill1(self):
        # print('通过slef获取name属性：',self.name)
        print("{}使用了技能：爬树".format(self.name))

    def skill2(self):
        print("使用了技能：抓老鼠")


c1 = Cat("叮当猫", "公猫", 18)

c2 = Cat("机器猫", "母猫", 1)


# 通过对象获取属性：对象.属性
# print(c1.attr1)
# print(c2.attr1)
# print(c1.name)

# 使用对象去调用方法：对象.方法名（）
# c1.skill1()
# c2.skill1()


# 属性的访问和方法的调用

# 对象可不可以访问类属性
# print(c1.attr1)   # 可以的
# # 对象可不可以访问对象属性
# print(c1.name)   # 可以的
# # 对象可不可以直接调用方法
# c1.skill1()     # 可以的

# 类可不可以访问类属性
# print(Cat.attr1)

# 类可不可以访问对象属性
# print(Cat.name)  # 不可以

# 类可不可以直接调用方法
# Cat.skill1()  # 不可以，会提示少一个参数slef


















# 不会按下面这个方式去操作
# Cat.skill1(Cat("叮当猫", "公猫", 18))





