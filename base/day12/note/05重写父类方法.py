"""
============================
Author:柠檬班-木森
Time:2020/1/20   21:00
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
在子类中定义和父类同名的方法：这个操作叫重写父类方法


# 需求一：v2版手机打电话升级为视频电话（v2中重写打电话的方法）
关于方法的调用：
    子类可以继承父类的方法，意味着子类可以调用父类的方法（父类不能调用子类的方法）
    如果子类重写了父类的方法，那么调用该方法时，优先调用自身的方法。


# 需求二：打了五秒钟视频电话之后，如果切换成语音通话。
关于在子类的方法中，如何调用被重写的父类方法（调用父类同名的方法）
    第一种方法：父类名.方法名（self）
    第二种方法：super().方法名（）



time模块中的sleep方法可以让程序休眠

"""

import time


# 需求一：
class BasePhone(object):
    def tell(self):
        print("这个是打语音电话的功能")


# 需求二
class PhoneV1(BasePhone):
    def send_msg(self):
        print("这个是发送短信的功能")

    def music(self):
        print("这个是播放音乐的功能")


# 需求三
class PhoneV2(PhoneV1):

    def game(self):
        print("这个是玩游戏的功能")

    def play(self):
        print("这个是支付的功能")

    def tell(self):
        print("这个是打视频电话的功能")
        time.sleep(5)  #  执行到这个代码，程序会暂停5秒
        # 第一种方法：父类名.方法名（self）
        # BasePhone.tell(self)

        # 第二种方法：super().方法名（）
        super().tell()


    def send_msg(self):
        print("这个是发送升级版的短信功能")


phone = BasePhone()
phone1 = PhoneV1()
phone2 = PhoneV2()

# phone.tell()
# phone1.tell()

phone2.tell()