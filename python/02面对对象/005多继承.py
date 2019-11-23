
class A:
    @staticmethod
    def test():
        print("test方法")
        pass
class B:
    def demo(self):
        print("的demo方法")
class C(A,B):

     pass

# 创建一个对象

c = C()
c.demo()
c.test()

# 查看c类对象调用函数过程·
print(C.__mro__)
