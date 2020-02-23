"""
============================
Author:柠檬班-木森
Time:2020/1/20   20:15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
类属性：定义在类里面的变量
    公有属性：在类外面通过类和对象都可以访问。
    
    私有属性：只能在类里面访问，类外面是不能去访问的。
        私有属性的定义：
            以单下划线开头：例如 _attr = 10(在类外面可以访问，但是大家不要去使用)
            以双下划线开头: 例如 __attr = 200（在类外面不能直接访问）
            扩展：双下滑开头的私有属性：在保存的时候对外其实换了个名字（__属性 --> _类名__属性）


"""


class TestClass:
    attr = 100
    _attr = 10
    __attr = 200

    def func(self):
        print(self._attr)
        print(self.__attr)





t1 = TestClass()
t1.func()

# 访问公有属性
# print(t1.attr)
# print(TestClass.attr)


# 访问单下换线开头的私有属性
# print(t1._attr)
# print(TestClass._attr)


# 访问双下换线开头的私有属性
# print(t1.__attr)
# print(TestClass.__attr)
# print(t1._TestClass__attr)
# print(TestClass._TestClass__attr)