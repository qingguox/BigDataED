class MusicPlayer(object):

    #  记录 第一个被创建对象的引用
    instance = None
    # 初始化标记
    init_flag = False
    def __new__(cls, *args, **kwargs):  # 类方法 静态方法

        # 1.判断类属性是否为空e
        if cls.instance is None:
            # 2.调用父类方法 ，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 3. 返回；类属性保存的对象引用
        return cls.instance

    def __init__(self): # 本来只执行一次  要求只有一次
        # 1. 判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return
        # 2. 如果没有执行过， 在执行初始化动作
        print("初始化播放器")
        # 3. 修改雷属性标记
        MusicPlayer.init_flag = True

# 创建对象
player1 = MusicPlayer() #player1和2地址一样这就是单例设计模式
print(player1)

player2 = MusicPlayer()
print(player2)
