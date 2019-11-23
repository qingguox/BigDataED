
'''
# python内置函数
# len() del() max() min()   "0"<"A"<"9"
# 字典和字典不能比较大小
#  运算符 [1.5]+[5.6] [1,2]*5 [1,2,1,2,1,2,1,2,1,2]
# 2 in [1,2,3] TRUE     3 not in [1,2,3]  FALSE
# in 在判断字典时 只能判断建

print("a" in {"a": "sdf", "b":"df"})
for num in [1, 2, 3]:
        print(num)
        if num == 5:
                break
        else:
        # 如果循环体内部使用break退出循环
        # else 就不会执行
            print("会执行吗？")
print("循环结束")

#字符串
字符串可以用’’定义和 ""定义

strl = "hello python "
str2 = "三大非农"
print(strl.count("llo"))
print(strl.index("llo"))
for i in strl:
    print(i, end="")

#字符串处理函数
#1，判断空白字符
space_str = "  \t\n\r"  #\t\n   \r是enter也属于空白字符
print(space_str.isspace())
#2.判断字符串中是否包含数字,都不能判断小数
#num_str = "\u00b2"   #Unicode 字符串  代表平方
num_str = "1"
num_str = "一千零一"
print(num_str.isdecimal())   #全角数字
print(num_str.isdigit())     #全角数字，(1),\u00b2
print(num_str.isnumeric())   #全角数字，汉子数字
num_str.istitle()      #是标题化的（每个单词的首字母大写）
num_str.islower()      #至少一个大小写字符，全为小写
num_str.isupper()      #至少一个大小写的字符，全为大学

#2.查找和替换
#1>判断是否已指定的字符串开始
hello_str = "hello world"
print(hello_str.startswith("hello"))
#2>判断是否已指定的字符串开始
print(hello_str.endswith("world"))
#3>查号
#  如果指定的字符串不存在，返-1
print(hello_str.find("llo"))
#4>替换
# replace 方法执行完成后，会返回一个新的字符串
#注意：不会修改原有字符串的内容
print(hello_str.replace("world", "python"))
print(hello_str)

# 3 文本  .ljust()  .rjust() .center()
#   括号内部为输出的字数不够，用空格补齐
poem = ["\t\n登黄鹤楼",
        " 王之涣",
        "白日依山尽\t\n",
        "黄河入水流",
        "欲穷千里目",
        "更上一层楼"
        ]
for poem_str in poem:
        #用strip方法去除字符串中的空白字符
        #在用center（）居中
    print("|%s|"%poem_str.strip().rjust(10, " "))
#  4去除空白字符  .lstrip() .rstrip() .strip()
#  5拆分和连接

poem_str1 = "登黄鹤楼\t王之涣\t 白日依山尽\t黄河入水流\t欲穷千里目\t更上一层楼"
#1 , 拆分字符串
poem_list = poem_str1.split()
print(poem_list)
#2 合并字符串
print(" ".join(poem_list))

#    6 字符串的切片
num_str6 = "012345678"
print(num_str6[1:5:2])
print(num_str6[::2])     #2为步长 相当于隔了一个数去
print(num_str6[2:-1])    #不包含-1位 也即是最后一位 8
print(num_str6[-2:])     #最后两位 78  步长默认为 1
print(num_str6[-1::-1])  #字符串倒叙 876543210 或[::-1]
'''

'''
#字典
#键   key 是索引
#值 value 是数据   字符串 ，数字，元组
#键 ：值 ,
#键必须是唯一的 {}
#字典是一个无序的数据集合  print输出时，顺序会有问题

xiaoming_dict= {"name": "小明",
            "age":45,
            "性别":"TURE"
            }
print(xiaoming_dict)
#字典操作
#1.取值
print(xiaoming_dict["name"])   #小明
#2.增加/修改
xiaoming_dict["age1"] = 18
xiaoming_dict["name"]  ="小小明"
#3.删除
xiaoming_dict.pop("age1")
#1.统计键值对的数量
print(len(xiaoming_dict))
#2.合并字典    注，如果被合并的字典中包含已经存在的键值对，则会覆盖
temp_dict ={"height":1.75}
xiaoming_dict.update(temp_dict)
#3.清空字典
xiaoming_dict.clear()
print(xiaoming_dict)
#遍历

xiaoming_dict= {"name": "小明",
            "age":45,
            "性别":"TURE"
            }
for k in xiaoming_dict:   #k 取得是键
    print("%s : %s "%(k, xiaoming_dict[k]))

#实际在开发过程中，常把多个字典放在列表中
card_list = [{"name": "张三",
              "qq": "2121"},
             {"name": "李四",
                "qq": "1515"}
             ]
for card_info in card_list:
    print(card_info)
    print(card_info["name"])
'''

'''
#元组
info_tuple = ("sadf",)  #元组中只有一个数据时 要在元素后加，逗号
info_tuple2 = ("asdf", 123, 6)
print(info_tuple)
print(info_tuple2[2])
#  元组的处理方法和列表差不多
#但是元组不允许修改
for intm in info_tuple2:
    print(intm)
#格式化字符串后面的（）本质就是元组
info_tuple1=("小明",20,185)
print("%s 年龄是 %d 身高是 %.2f"%("小明",20,185))
print("%s 年龄是 %d 身高是 %.2f"%info_tuple1)

info_str ="%s 年龄是 %d 身高是 %.2f"%info_tuple1
print(info_str)

#元组和列表的转化
num_list = [1,2,3,4]
num_tuple= tuple(num_list)
print(num_tuple)

num2_list = list(num_tuple)
print(num2_list)

#列表操作
name_list = [12,13,1,56]
name_list22=["我的美人","爱人"]
#1.取值和取索引
print(name_list[0])
print(name_list.index(56))
#2.修改
name_list[0]= 45
#3，增加
name_list.append(89)  #从表后添加
name_list.insert(1,"dfgh")   #按照下标插入
name_list.extend(name_list22)   #从表后插入一个新的列表
#4，删除
name_list.remove("爱人")     #删除指定的数据   del name_list[2]
name_list.pop()             #删除表尾元素
name_list.pop(3)           #删除指定元素的下标
#name_list.clear()          #清空表
#5.表长 及数据计数
print(len(name_list))
print(name_list.count(56))     #数据出现的次数
print(name_list)
#6.升序 降序 反转
name_list5 = [12,13,1,56]
name_list5.sort()      #升序
print(name_list5)
name_list5.sort(reverse = True)   #降序
print(name_list5)
name_list5.reverse()     #反转
print(name_list5)

#迭代遍历
for name in name_list5:

    print("我的数据 :%d"%name)
'''
'''
def print_line(char ,time ):
    print(char *time)
def mulitiple_tabl():
    """"xcvghjkl"""

    i = 1
    while i<=9:
        j = 1
        while j<=i:
            print("%d * %d = %d  \t"%(j,i,i*j),end="")   #end = ""不让其换行
            j +=1
        print("")   #换行
        i+=1
mulitiple_tabl()
print_line("_",50)
'''
'''
password = input("亲输入密码：")   #input 所输入的都是字符串吧 也即是password为字符产
print(password)

type(password)

name = "小明"
student_no = 2
print("我得名字叫：%s ，学号是 %d"%(name ,student_no) )

import keyword
print(keyword.kwlist)
'''

'''
注意  python3 使用filter map reduce
sn = reduce(lambda x,y: x+y, sn)

要引用 from functools import reduce

'''

#*nums **pers 接受元组 和 字典
def demo(num,*nums,**person):

    print(num)
    print(nums)
    print(person)
    #1 () {}
demo(1)
demo(1,2,3,4, name = "小明", age = 18)
'''
# 11111注意  对于列表   相当于对象 其操作函数会改变其的值
def demo(num_list):
    num_list.append(9)
    print(num_list)
    num_list.extend([5,3])
    #等同于 += 调用了 extend方法 改变
    #  而 = +时不会改变
gl_list = [1,2,6]
demo(gl_list)
print(gl_list)
#11111111111111111给缺省参数赋值
def print_info(name, gender=True):
    #gender = bool类型
    gender_test = "男生"
    if not gender:
        gender_test = "女生"
    print("%s 是 %s "% (name, gender_test))

print_info("小明",True)
print_info("小美",False)

# python中的变量 变量与值是一种引用关系 给
# 给变量重新赋值  相当于 把a  指向后面这个值
# a的地址在赋值后发生改变
a = [1,2,3]

b = a # 相当于 b和 a同时应用 列表 [1,2,3]

# 重新给a 赋值 a就会指向 55的空间 断开了列表
a  = 55
print(b, a)

# 注意 字典 key只能是不可改变数据类型   字符串 数字 元组
#  字典 和 列表为 可变类型

# 全局变量 局部变量
#  如果 要再函数内部修改全局变量 要在函数内部 加global

num = 10
def print5():


    global num # 注意 要修改了
    num = 100
    print(num)
def print88():

    print(num)  # 测试 全局变量是否被修改
print5()
print88()

# 函数返回
def jj():
    jj = 55
    pp = 88
    return jj,pp   # 相当于 return (jj,pp)
                    # 基本都是默认返回元组
mm = jj()
l_jj,l_pp = jj()    # 多个变量 接受返回
print(l_jj,l_pp)
print(mm)

# 交换两个数字
a = 5
b = 9
# a = a+b
# b = a-b
# a = a-b
# 或者
a,b = b,a  # (b,a) 元组
print(a,b)
'''