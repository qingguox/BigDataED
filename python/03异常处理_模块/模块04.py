
import wfu as DU # 1.导入 wfu 文件 并命名为DU

#DU.main()

# 2. 导入一部分工具
from wfu import main

# 3.导入不同模块中同名函数时  会覆盖的先前函数

#4. 导入 所有工具
from wfu import *

# 5. 给文件起名时  不要与系统文件名一样
# 每个模块内 都有一个内置函数 __file__
import  random

rand = random.randint(0, 10)
print(rand)
print(random.__file__)

# 6.当导入一个模块时 这个模块内所有没被缩进的语句都执行一边


# 在模块内 如果直接执行模块 ， __main__
if __name__ == "__main__":
    # __name__ 就是"__main__"
    #  但是在其他导入这个文件中 文件铭.__name__ 则是文件铭
    main()
    pass
