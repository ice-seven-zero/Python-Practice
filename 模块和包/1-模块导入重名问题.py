#如果两个模块，存在同名的函数，那么后导入模块的函数，会覆盖掉先导入的函数
from module1 import test01
from module2 import test01 as test02#用as对模块起别名
#from module1 import test01相比于import module1，可以使module1.test01()简写成test01()

import random
test01()
test02()
print(random.__file__)#Python 中每一个模块都有一个内置属性__file__可以查看模块的完整路径