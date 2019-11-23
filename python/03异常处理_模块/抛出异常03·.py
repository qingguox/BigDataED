
def input_password():

    # 1. 提示用户输入密码
    pw = input("请输入密码：")
    # 2.判断密码长度 >=8 返回密码
    if len(pw) >= 8:
        return pw
    # 3. <8 抛出一个异常
    # 1.>先创建一个异常对象 可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够")
    # 2.>抛出
    raise ex
try:

    print(input_password())
except Exception as result:
    print(result)  # 接收的异常字符串  密码长度不够