"""
============================
Author:柠檬班-木森
Time:2020/1/13   21:49
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
第一种：导入模块
import  模块名
不能使用import 包名/文件夹

第二种：导入模块中的某个函数或者变量
from 模块名 import 变量或函数


第三种：导入的时候给导入的内容起别名
from 模块 import 变量或函数 as 别名

from  文件夹.文件夹 import 模块 as 别名


# 第四种： 几乎不用，也不推荐用的导入方式(代码可读性不高)

from 模块 import *          # 导入指定模块中所有的变量和函数

from 文件夹.文件夹 import *     # 导入指定文件夹中所有的模块

"""

# from login import a
# from py26_09day.practice.login import login_func,a
#
# # print(a)
# login_func()

# 给导入的内容起别名
# from py26_09day.practice.login import login_func as lg
#
# lg()

#
# from py26_09day.practice.login import login_func
#
# from py26_09day.practice.register import register_func

# 不推荐使用
# from py26_09day.practice.login import *
# from py26_09day.practice.register import *
#
# login_func()

# 课后独立思考：
#  在进行模块导入的时候，会将导入的模块从上到下执行一遍，
#  问题一：如果有一部分代码在导入的时候不希望执行的应该怎么处理？
#
#
# 问题二：包里面的__init__.py到底有什么用？