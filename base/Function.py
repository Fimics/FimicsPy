def print_info():
    print("function")


print_info()


def add(a, b):
    return a + b


print(add(1, 2))
print(add(a=12, b=2))

"""
全局变量<-->局部变量
在函数外边定义的变量叫做全局变量
全局变量能够在所有的函数中进行访问
如果在函数中修改全局变量，那么就需要使用global进行声明，否则出错
如果全局变量的名字和局部变量的名字相同，那么使用的是局部变量的，小技巧强龙不压地头蛇
"""


# 在python中我们可不可以返回多个值？
def divid(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu


print(divid(16, 5))

'''
 缺省参数
 调用函数时，缺省参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：
 带有默认值的参数一定要位于参数列表的最后面。

'''


def printinfo1(name, age=35):
    # 打印任何传入的字符串
    print("Name: ", name)
    print("Age ", age)


# 调用printinfo1函数
printinfo1(name="miki")
printinfo1(age=9, name="miki")

"""
不定长参数
加了星号（*）的变量args会存放所有未命名的变量参数，args为元组；
而加**的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典。
"""


def fun(a, b, *args, **kwargs):
    print("a=", a)
    print("b=", b)
    print("args=", args)
    print("kwargs")
    for key, value in kwargs.items():
        print(key, "=", value)


fun(1, 2, 3, 4, 5, m=6, n=7, p=8)

c = (3, 4, 5)
d = {"m": 6, "n": 7, "p": 8}
fun(1, 2, *c, **d)

sum = lambda x, y: x + y

print(sum(2, 3))


# 函数作为参数
def fun1(a, b, opt):
    return opt(a, b)


result = fun1(33, 22, lambda x, y: x + y)
print(result)
