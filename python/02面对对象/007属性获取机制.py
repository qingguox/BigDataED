class Tool:

    count = 0 #类属性 记录所有工具对象的数量

    def __init__(self, name):
        #   类对象属性   在tool2.count如果对象没有count 就会向上查找
        # 称为 向上转型
        self.name = name
        #只会给对象添加一个属性
        # 不会影响类属性

        # 让类属性 的值++1
        Tool.count +=1
# 1. 创建工具类
tool1 = Tool("斧头")  #创建一个对象 只会拥有name属性
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# 2. 输出工具对象的总数
print(Tool.count)
# print(tool2.count) # 不建议  python解释器 发现对象没有count 向上查找类中的 但不会给tool2添加属性

tool3.count = 99  # 赋值时  python解释器 发现对象没有count 所以新建了一个count属行 并赋值为99
print("工具总数为： %d" % tool3.count)   #99
print("类属性 count为：%d "% Tool.count)  # 3
