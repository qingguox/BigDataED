class A:

    def __init__(self):  # 私有方法
        self.num1 = 100    #公有属性
        self.__num2 = 200 #私有属性
    def __test(self):       # 私有方法
        print("私有属性 %d %d" % (self.num1, self.__num2))

    def test(self):         #公有方法
        print("父类的公有方法 %d" % self.__num2)

class B(A):
    def demo(self):
        # 1. 访问 父类 的公有属性
        print("子类方法 %d" % self.num1)
        # 2. 调用父类的公有方法
        self.test()    # 间接访问父类私有属性
        # 3.不能访问 父类的私有属性 / 方法
        pass
    # def test(self):
    #
    #     print("zilei1 test")
        pass
#创建一个子类对象
b= B()

#在外界访问父类 的公有属性/调用公有方法
print(b.num1)
b.test()
b.demo()

'''
1.子类对象不能在自己的方法内部 直接访问父类的私有属性或私有方法
2.子类对象 可以通过 父类的公有方法间接访问 私有属性或私有方法
class Animal:
    def eat(self):
        print("吃")
    def bark(self):
        print("叫")
class Dog(Animal):             #继承
    def drink(self):
        print("喝")
    def bark(self):      # 覆盖 重写
        # 1. 针对子类的有的需求  ，编写代码
        print("汪汪叫")
        #2. 使用super().  调用原本在父类中封装的方法
        # super().bark()
        # 父类名.方法（self）
        Animal.bark(self)
        # 3. 增加其他子类的方法
        print("asdf")
        pass
d = Dog()
d.drink()  # 子类方法
d.eat()  # 基类的方法
d.bark()
'''

















