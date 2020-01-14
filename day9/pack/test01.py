"""
============================
Author:柠檬班-木森
Time:2020/1/13   21:35
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
注意点：
1、模块导入的时候，同级目录导入，pycharm有可能识别不了，会对代码进行标红（不代表报错）

2、在进行模块导入的时候，会将导入的模块从上到下执行一遍
"""

# 同级目录下的模块可以直接使用import进行导入（pycharm有可能识别不了）
# import register

# 从项目目录下，一级一级往下导入
from py26_09day.pack.pack02 import register03


# 可以直接导入python安装路径下的模块（几乎不会使用该方式）
# import register02


# register02.register_func()






