"""
============================
Author:luli
time:2020/1/19
company:happy
============================
"""

'''
1、类属性怎么定义？ 实例属性怎么定义？
'''


# 类属性：直接定义在类里面的变量
class Student:
    task = 'study'


# 实例属性：
# 方法1：通过对象进行赋值
student1 = Student()
student1.name = 'xiaohong'


# print(student1.name)
# print(student1.task)


# 方法2：过初始化方法__init__进行定义

class Car:
    skill = 'run'

    def __init__(self, name):
        self.name = name


car1 = Car('Lamborghini')
# print(car1.name)
# print(car1.skill)

'''
2、实例方法中的self代表什么？（简答）

-----self代表的是对象本身，哪个对象去调用方法，self代表的就是哪个对象
'''

'''
3、类中__init__方法在什么时候会调用的？（简答）

------创建对象的时候自动调用    
'''

'''

4、封装一个测试用例类(自行分辨定义为类属性还是实例属性)，
-  属性：用例编号  url地址   请求参数   请求方法    预期结果   实际结果
用例编号：01
url地址：https://tcc.taobao.com/cc/json/mobile_tel_segment.htm
请求参数：tel=
请求方法：get
预期结果：
实际结果:
'''


class OpenUrl:
    def __init__(self, case_id, url, param, method, excepted, actual):
        self.case_id = case_id
        self.url = url
        self.param = param
        self.method = method
        self.excepted = excepted
        self.actual = actual


case1 = OpenUrl('01', 'https://tcc.taobao.com/cc/json/mobile_tel_segment.htm', 'tel=13065708888', 'GET', '测试通过', '测试通过')
'''

5、封装一个学生类，(自行分辨定义为类属性还是实例属性，方法定义为实例方法)
-  属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
-  方法一：计算总分，方法二：计算三科平均分，方法三：打印学生的个人信息：我的名字叫XXX，年龄：xxx,性别：xxx。
'''


class Student:
    identity = 'student'

    def __init__(self, name, age, sex, en_score, math_score, ch_score):
        self.name = name
        self.age = age
        self.sex = sex
        self.en_score = en_score
        self.math_score = math_score
        self.ch_score = ch_score

    def total(self):
        try:
            total_score = self.en_score + self.math_score + self.ch_score
        except Exception as e:
            print(e)
        else:
            return total_score

    def average(self):
        try:
            aver_score = round((self.en_score + self.math_score + self.ch_score) / 3, 2)
        except Exception as e:
            print(e)
        else:
            return aver_score

    def print_info(self):
        stu_info = f'我的名字叫{self.name}，年龄：{self.age},性别：{self.sex}'
        print(stu_info)


stu1 = Student('ly', '18', 'nv', 95, 76, 98)
# print(stu1.total())
# print(stu1.average())
# stu1.print_info()
