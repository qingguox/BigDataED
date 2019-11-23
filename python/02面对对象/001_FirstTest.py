'''
class Cat:
    def __init__(self): # 初始化
        print("自动调用")
        self.name = "mm" #在初始化·方法中定义属性
    def eat(self): # self: <__main__.Cat object at 0x00000153557499E8>
        #哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 爱吃鱼"% self.name)
    def drink(self):
        print("%s 喝水"% self.name1)

# 创建猫对象 然后 tom指向这个对象
# 之后 初始化方法 self指向这对象 建立name1属性
tom = Cat()
#添加属性
tom.name1 = "Tom"
tom.eat()
tom.drink()

class Cat:

    def __init__(self, new_name):
        print("这是一个初始化方法")

        self.name = new_name
    def eat(self):
        print("%s 爱吃鱼"% self.name)

    def __del__(self):
        print("释放空间 析构")

    def __str__(self):
        return "我是小猫：%s "% self.name
tom = Cat("Tom")
#print(tom.name)
#tom.eat()
print(tom)   #本来是输出 对象的内存地址 用 str后就输出自定义内容
# del 可以删除一个对象
# del tom
print("-"*50)


class Person:

    def __init__(self, name, weight):

        self.name = name
        self.weight = weight
    def __str__(self):
        return "我的名字叫 %s 体重为：%.2f"% (self.name, self.weight)

    def eat(self):
        self.weight += 1
    def run(self):
        self.weight -= 0.5

p1 = Person("小明", 75.0)
p1.eat()
p1.run()
print(p1)

p2 = Person("小美",50)
p2.eat()
p2.run()
print(p2)
'''

class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area
    def __str__(self):
        return "[%s] 占地 %.2f"% (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        #家具名称列表
        self.item_list = []
    def __str__(self):
        return ("户型 ：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"\
               % (self.house_type, self.area,
                  self.free_area, self.item_list))
    def add_item(self, item):
        print("要添加 %s" % item.name)
        #1.判断家具面积
        if item.area > self.free_area:
            print("%s 面积太大，无法添加"% item.name)
            return
        #2.将家具的名称添加
        self.item_list.append(item.name)
        #3.计算剩余面积
        self.free_area -= item.area

bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

#print(bed)
#print(chest)
#print(table)

# 创建 房子对象
my_home = House("两室一厅", 60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)



class Person:

    def __init__(self, name, score):

        self.name = name
        self.frea = score - 20
        self.ll = 20

    def __str__(self):
        return ("%s : 分数 score %d"%(self.name , self.frea))

    def __del__(self):
        print("清除对象 %s"%(self.name))

    def test(self):

        print(self.frea)

    def __kk(self):
        print("私有函数 ")


p = Person("adf", 80)
print(p)
print(p.frea)
print(p.ll)
p._Person__kk()   # 调用私有函数
#
# 私有变量:实例._类名__变量名
# 私有方法:实例._类名__方法名()
del p

