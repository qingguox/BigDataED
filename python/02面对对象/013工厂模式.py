'''
工厂模式

相当于 创建工厂类   调用静态或者 类方法

'''

class Person(object):

    def __init__(self, name):

        self.name = name;

    def userUsers(self, type):

        print(self.name, "开始工作了！")

        axe = Factory.getAxe(type)
        axe.work()


class Axe(object):

    def __init__(self,name):
        self.name = name
        pass
    def work(self):
        print("使用", self.name, "砍树")

class stone(Axe):


    def __init__(self):
        pass
    def work(self):
        print("使用石斧砍树")

class stell(Axe):

    def __init__(self):
        pass
    def work(self):
        print("使用钢铁砍树")

class Factory(object):

    @staticmethod
    def getAxe(type):

        if "stone" == type:
            return stone()
        elif "stell" == type:
            return stell()
        else:
            print("参数出错！1.。。")

p = Person("zhansna1 ")
p.userUsers("stell")