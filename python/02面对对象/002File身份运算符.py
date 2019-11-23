
class Gun:

    def __init__(self, model):
        #1.枪的型号
        self.model = model
        #2. 子弹的数量
        self.buller_count = 0
    def add(self, count):

        self.buller_count +=count
    def shoot(self):
        #1.判断子弹数量
        if self.buller_count <= 0:
            print("[%S] 没有子弹了。。。"% self.model)
            return
        # 2.发射子弹
        self.buller_count -=1

        # 3.提示发射信息
        print("[%s]突突-----------[%d]"% (self.model,self.buller_count))


class Soldier:

    def __init__(self, name):

        self.name = name
        self.gun = None
    def fire(self):
        if self.gun == None: # 等价于  self.gun is None
            print("%s 没有枪\n")
            return
        # 1. 装填子弹
        self.gun.add(50)
        # 2. 发射子单
        self.gun.shoot()

    def __str__(self):
        return "%s 有枪: %s" % (self.name, self.gun.model)

# 1。抢对象
ak47 = Gun("ak47")
# 2 s士兵·1
X = Soldier("许三多")
X.gun = ak47    # 一个类的属相可以是 另一个类创建得对象
X.fire()
print(X)