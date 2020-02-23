"""
============================
Author:luli
time:2020/1/24
company:happy
============================
"""

'''
1、 用户登陆程序需求:
1.	输入用户名和密码;
2.	判断用户名和密码是否正确? (name='python', passwd='lemonban')
3.	为了防止暴力破解， 登陆仅有三次机会， 如果超过三次机会， 提示错误次数过多，账号已被冻结,;
'''


def login():
    user_info = {'name': 'python', 'passwd': 'lemonban'}
    for i in range(1, 4):
        name = input('请输入用户名：')
        passwd = input('请输入密码：')
        if name == user_info['name'] and passwd == user_info['passwd']:
            print('登陆成功')
            break
        else:
            print('账号或密码错误,您还有{}次机会'.format(3 - i))

    else:
        exit('错误次数过多，账号已被冻结')


# login()

'''
2、给定一个句子（只包含字母和空格）， 将句子中的单词位置反转， 比如： “hello xiao mi” > “mi xiao hello”
'''


def reverse_wd(sentence):
    sentence = sentence.split(' ')
    sentence.reverse()
    sentence = ' '.join(sentence)
    print(sentence)


# reverse_wd('hello xiao mi')


'''
3、运行程序，提示用户依次输入三个整数x,y,z，请把这三个数由小到大输出。
'''


def sort_num():
    x = int(input('请输入第一个整数：'))
    y = int(input('请输入第二个整数：'))
    z = int(input('请输入第三个整数：'))
    list1 = [x, y, z]
    list1.sort()
    print(list1)


# sort_num()

'''
4、编写一个程序，使用for循环输出0-100之间的偶数
'''


def output_num():
    for i in range(0, 102, 2):
        print(i)


# output_num()

'''
5、打开一个文本文件，读取其内容，把其中的大写字母修改为小写字母，再写入文件覆盖原内容。
'''


def lower_letter():
    try:
        with open('test.txt', 'r+', encoding='utf-8') as f:
            content = f.read()
    except:
        print('文件不存在')
    else:
        content = content.lower()
        with open('test.txt', 'w', encoding='utf8') as f:
            f.write(content)
        print('运行成功')


# lower_letter()

'''
6、现在有一个字符串s = 'asdf2273788hh90999',请写一段代码来删除字符串中的重复元素，最后转换为列表保存。
'''

s = 'asdf2273788hh90999'
s = set(s)
s = list(s)
# print(s)

'''
7、小明有100块钱 ，需要买100本书（钱要刚好花完），a类数5元一本，b类书3元一本，c类书 1元2
本。请计算小明有多少种购买的方式？
'''


def buy_book():
    num = 0
    for i in range(0, 100 // 5 + 1):
        for j in range(0, 100 // 3 + 1):
            h = 100 - i - j
            if i * 5 + j * 3 + h * 0.5 == 100:
                num += 1
                print('第{}种方式：a类{}本，b类{}本，c类{}本'.format(num, i, j, h))

    print(num)


# buy_book()

'''
8、题目：小明买了一对刚出生的兔子，兔子从出生后第3个月起每个月都生一对兔子，生的这对小兔子长到第三个月也开始生兔子（每个月生一对兔子），
假如兔子都不死，问10个月后小明的兔子为多少对？（思路提示：重点在分析出兔子增长的规律，分析出规则之后通过for循环即可实现）？ 
'''


def buy_rabbit():
    total_list = []
    for i in range(1, 11):
        if i == 1 or i == 2:
            num = 1
        else:
            num = total_list[i - 3] + total_list[i - 2]
        total_list.append(num)
        print(total_list)
    print(total_list[-1])


# buy_rabbit()


'''
9、请封装一个函数，来实现要求的数据格式转换功能（思路提示：for循环和zip函数）：
# 数据转换有一组用例数据如下：
cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]
# 需要转换为以下格式：
cases02 = [{'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
           {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
           {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
           {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
           {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]

'''


def transform_data():
    cases = [
        ['case_id', 'case_title', 'url', 'data', 'excepted'],
        [1, '用例1', 'www.baudi.com', '001', 'ok'],
        [2, '用例2', 'www.baudi.com', '002', 'ok'],
        [3, '用例3', 'www.baudi.com', '002', 'ok'],
        [4, '用例4', 'www.baudi.com', '002', 'ok'],
        [5, '用例5', 'www.baudi.com', '002', 'ok'],
    ]
    cases02 = []
    title = cases[0]
    cases.pop(0)
    for item in cases:
        case = zip(title, item)
        case = dict(case)
        cases02.append(case)
    print(cases02)


# transform_data()

'''           
10、题目：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时，高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于
100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''


def bonuses():
    try:
        profits = float(input('请输入当月的利润：'))
    except:
        print('请输入数字')
    else:
        if profits <= 100000:
            bonus = profits * 0.1
        elif profits < 200000:
            bonus = 100000 * 0.1 + (profits - 100000) * 0.075
        elif profits < 400000:
            bonus = 100000 * 0.1 + 100000 * 0.075 + (profits - 200000) * 0.05
        elif profits < 600000:
            bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (profits - 400000) * 0.03
        elif profits < 1000000:
            bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 400000 * 0.03 + (profits - 600000) * 0.015
        else:
            bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 400000 * 0.03 + 600000 * 0.015 + (
                    profits - 1000000) * 0.01
        print(bonus)


# bonuses()

''' 
11、编写一个自动售货机，运行功能如下:
1、请按下面提示，选择购买的商品
1). 可乐 2.5元 2). 雪碧 2.5元 3). 哇哈哈 3元 4). 红牛 6元 5). 脉动 4元 6). 果粒橙 3.5元
2、提示用户投币（支持1元，5元，10元）
用户输入投币金额，
用户投币金额不够商品价格，继续提示投币，
当投币超过商品价格，则返回商品和找零，然后结束程序
'''


def sale():
    print('''--------请按下面提示，选择购买的商品------
    1). 可乐 2.5元 
    2). 雪碧 2.5元 
    3). 哇哈哈 3元 
    4). 红牛 6元 
    5). 脉动 4元 
    6). 果粒橙 3.5元
-----------------------------------------
    ''')
    goods = {'可乐': 2.5, '雪碧': 2.5, '哇哈哈': 3, '红牛': 6, '脉动': 4, '果粒橙': 3.5}
    res = enumerate(goods)
    num = int(input('请输入您需要购买的商品编号：'))
    for item in res:
        if item[0] + 1 == num:
            good = item[1]
            price = goods[item[1]]
            print(f'您购买的商品为{good}，价格为{price}元')
            money = 0
            while money < price:
                m = input('请投币（支持1元，5元，10元）：')
                if m in ['1', '5', '10']:
                    money += int(m)
                else:
                    print('您投入的金额有误或者不支持该面额')
            else:
                balance = round(money - price, 1)
                print(f'您购买的商品为{good}，价格为{price}元，您投入的金额为{money}元,剩余{balance}元')
                return good, balance
    else:
        exit('您输入的商品编号有误')


# sale()

''' 
12、封装一个老师类
属性：姓名 年龄 性别 授课科目 授课班级（list类型，可以保存多个班级） 
方法： 添加授课班级 、 打印老师的信息
'''


class Teacher:
    def __init__(self, name, age, sex, subject, classes):
        self.name = name
        self.age = age
        self.sex = sex
        self.subject = subject
        self.classes = classes

    def add_class(self, classes):
        self.classes.append(classes)

    def print_info(self):
        print('姓名：{}，年龄：{}，性别：{}'.format(self.name, self.age, self.sex))


''' 
13、类和继承
要求一：定义一个游戏英雄类（Hero） 
特征（属性）：名字（name）、血量（HP）
行为（方法）：技能1：移动 
要求二：定义一个战士类（继承英雄类）
除了上面英雄类的属性之外，还多了一个属性：攻击力（attack）和一个方法：技能2（普通攻击）
要求三：定义一个法师类（继承英雄类）
除了上面英雄类的属性之外，还多了一个属性：法力值（MP）和一个方法：技能2（法术攻击）

'''


class Hero:
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP

    def skill1(self):
        print('技能1：移动')


class Warrior(Hero):
    def __init__(self, MP, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.MP = MP

    def skill2(self):
        print('技能2：普通攻击')


class Mage(Hero):
    def __init__(self, attack, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attack = attack

    def skill3(self):
        print('技能3：法术攻击')


Arthur = Warrior(100, 'Arthur', 120)
# print(Arthur.name)
# print(Arthur.MP)
# print(Arthur.HP)
# Arthur.skill1()
# Arthur.skill2()
