
class Dog(object):

    @staticmethod
    def run():  # 静态方法不需要访问类属性或者对象属性

        print("小狗跑。。。")
        pass
# 类名.调用   不需要创建对象
Dog.run()

