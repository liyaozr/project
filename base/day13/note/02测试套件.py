"""
============================
Author:柠檬班-木森
Time:2020/2/3   20:42
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
测试套件：使用unittest.TestSuite这个类创建出来的对象就是测试套件


测试运行程序：使用unittest.TextTestRunner创建出来的对象，就是一个测试用例运行程序对象（执行用例的入口）
    - 测试运行程序后面会用第三方的，不使用unittest自带的


用例加载对象：unittest.TestLoader


测试用例执行的顺序：根据用例的方法名，安装ASCII码进行排序的（不是根据定义的先后顺序）


"""
import unittest
# from py26_13day.testcases import LoginTest


# 第一步：创建一个测试套件
suite = unittest.TestSuite()

# 第二步：将测试用例加载到测试套件中
# 第一种：一条一条添加
# 创建测试用例对象
# case1 = LoginTest("test_login_pass")
# case2 = LoginTest("test_user_is_none")
# # 将用例添加到套件
# suite.addTest(case1)
# suite.addTest(case2)

# 第二种:通过测试用例类进行添加
# 创建一个用例加载对象
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(LoginTest))

# 第三种:通过用例模块去加载测试用例
from py26_13day import testcases
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(testcases))


# 第四种:通过路径去进行加载（默认会加载该路径下面所有以test开头的模块中的测试用例,可以通过pattern这个参数指定模块名匹配规则）
# loader = unittest.TestLoader()
# suite.addTest(loader.discover(r"C:\project\py26_project\py26_13day",pattern="case*"))

# unittest中的默认加载器对象（扩展）
# unittest.defaultTestLoader.

# 第三步：执行测试用例（需要先创建一个测试运行程序）
# 创建测试运行程序
runner = unittest.TextTestRunner()

# 执行测试套件中的测试用例
runner.run(suite)