
class A:

    def __init__(self, name):  #私有方法

        self.name = name  #公有属性
        self.__age = 18   # 私有属性 __+名

    def secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))
xiao = A("小芳")
xiao.secret()
## 私有属性  再类外不可访问print(xiao.__age)
print(xiao.name)
print(xiao._A__age)   #_类 + 私有属性 可访问哦

