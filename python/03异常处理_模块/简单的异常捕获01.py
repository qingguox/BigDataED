


try:
    num = int(input("请输入一个整数："))
    result = 8/num
except ZeroDivisionError:
    print("除0错误")
    pass
except ValueError:
    print("请输入正确的整数")

except Exception as result:    # 其他为止异常
    print("未知错误 %s" % result)

else :
    # 没有异常·才会执行
    print("asdf")
finally:
    # 无论是否有异常 都会执行
    pass
print("-"*52)