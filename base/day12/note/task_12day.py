"""
============================
Author:柠檬班-木森
Time:2020/1/19   9:37
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
1、类属性怎么定义？ 实例属性怎么定义？
    类属性定义：直接定义在类里面的变量
    实例属性定义：对象.属性名 = 属性值


2、实例方法中的self代表什么？（简答）
    self代表对象本身（自己），哪个对象调用这个方法就代表那个对象。


3、类中__init__方法在什么时候会调用？（简答）
    创建对象的时候会自动调用


4、封装一个学生类，(自行分辨定义为类属性还是实例属性)

-  属性：，身份(学生) 姓名，年龄，性别，英语成绩，数学成绩，语文成绩，

-  方法一：计算总分，方法二：计算三科平均分，方法三：打印学生的个人信息。


5、封装一个测试用例类(自行分辨定义为类属性还是实例属性)，

-  属性：用例编号  url地址   请求参数   请求方法    预期结果   实际结果



get  post  patch delete  put

"""


# 第四题：

class Students:
    """学生类"""
    identity = "学生"

    def __init__(self, name, age, gender, english, number, chinese):
        self.name = name
        self.age = age
        self.gender = gender
        self.english = english
        self.number = number
        self.chinese = chinese

    def sum_score(self):
        """计算总分"""
        res = self.english + self.number + self.chinese
        # self.sum = res
        return res

    def avg_score(self):
        """计算平均分"""
        res = (self.english + self.number + self.chinese) / 3
        return res

    def desc_info(self):
        """打印信息"""
        print('学员名字：{}，年龄：{}，性别：{}....'.format(self.name, self.age, self.gender))


s1 = Students("小明", 18, "男", 80, 98, 88)
res_sum = s1.sum_score()
print("总成绩：",res_sum)
res2 = s1.avg_score()
print("平均成绩：",res2)
s1.desc_info()


s2 = Students("小红", 17, "女", 90, 99, 98)
res_sum = s2.sum_score()
print("总成绩：",res_sum)
res2 = s2.avg_score()
print("平均成绩：",res2)
s2.desc_info()

# 第五题

class Cases:
    """用例类"""

    def __init__(self, case_id, url, data, method, excepted, actual):
        self.case_id = case_id
        self.url = url
        self.data = data
        self.method = method
        self.excepted = excepted
        self.actual = actual

# 类属性：类和实例对象都可以调用
# 实例属性：只要实例对象才能够调用

