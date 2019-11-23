class Tool:
    count = 0 #类属性 记录所有工具对象的数量

    @classmethod
    def show_tool_count(cls): # 类方法 cls类
        #cls. 访问类属性 和其他类方法
        print("工具对象的数量 %d" % cls.count)
        pass

    def __init__(self, name):  #self ==每个对象
        self.name = name
        # 让类属性 的值++1
        Tool.count +=1
# 1. 创建工具
tool1 = Tool("斧头")  #创建一个对象 只会拥有name属性
tool2 = Tool("榔头")
tool3 = Tool("水桶")

Tool.show_tool_count()