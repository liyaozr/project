"""
============================
Author:柠檬班-木森
Time:2020/2/10   21:27
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
conf.ini


"""
from configparser import ConfigParser

# 第一步创建一个配置文件解析对象
conf = ConfigParser()

conf.read("conf.ini")

# 读取配置文件中的内容
# 第一个get方法:读取出来的都是字符串类型
# 参数一：配置区域（块）  参数二：配置项
# res = conf.get("mysql", "port")
# print(res,type(res))

# 第二个方法：getint:获取数字类型的数据(int类型)
# res = conf.getint("mysql", "port")
# print(res,type(res))

# 第三个方法：getfloat:获取浮点数
# res = conf.getfloat("mysql", "test_data")
# print(res, type(res))

# 第四个方法：getboolean:获取布尔值
# res = conf.getboolean("mysql","test")
# print(res,type(res))

# 扩展
# 获取所有的配置区域（块）
# res1 = conf.sections()
# print(res1)

# 获取配置块下的所有配置项
# res2 = conf.options("mysql")
# print(res2)

# 获取配置块下的所有配置项
# res3 = conf.items("mysql")
# print(res3)


# 数据写入：set方法
# conf.set("mysql", "name", "MuSen")
# # 写入到文件:注意点：使用w模式去写入
# conf.write(fp=open("conf.ini", "w"))
