"""
============================
Author:柠檬班-木森
Time:2020/1/20   21:00
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
- ###### 需求V1：实现一个初始版的手机类（大哥大）

    - ###### 只能打电话

- ###### 需求V2：实现一个定义功能机类

    - ###### 打电话，听音乐，发短信

- ###### 需求V3：实现一个智能手机类

    - ###### 打电话，听音乐，发短信，看视频，玩游戏、手机支付）



继承关系：
    通过继承可以获得父类的方法和属性

    私有的属性时不能继承的（双下划线的不能）。  



"""


# 需求一：
class BasePhone(object):
    attr = "手机"
    __name = "大哥大"

    def tell(self):
        print("这个是打电话的功能")

    def print_name(self):
        print("手机的名字为",self.__name)


# 需求二
class PhoneV1(BasePhone):
    def send_msg(self):
        print("这个是发送短信的功能")

    def music(self):
        print("这个是播放音乐的功能")

    def print_name1(self):
        print("手机的名字为",self.__name)


# 需求三
class PhoneV2(PhoneV1):

    def game(self):
        print("这个是玩游戏的功能")

    def play(self):
        print("这个是支付的功能")

    def print_name2(self):
        print("手机的名字为", self.__name)


phone = BasePhone()
phone1 = PhoneV1()
phone2 = PhoneV2()
# phone1.tell()
# phone2.tell()

# 继承属性
# print(phone.attr)
# print(phone1.attr)
# print(phone2.attr)


# 私有属性的继承问题
# phone.print_name()


# 私有属性继承不了
# phone1.print_name1()
# phone2.print_name2()