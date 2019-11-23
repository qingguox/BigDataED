class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍 " % self.name)
    pass


class XiaoTiaoDog(Dog):

    def game(self):
        print("%s 飞到天上玩耍 、、、" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):

        print("%s 和  %s 快乐的玩耍 " % (self.name, dog.name))

        # 让狗 玩耍
        dog.game()
# 狗对象
# waqngcai = Dog("旺财")
wangcai = XiaoTiaoDog("哮天犬")
# 人对象
xiaoming = Person("小明")
# 玩
xiaoming.game_with_dog(wangcai)

