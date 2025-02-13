"""
可以有零个或多个elif部分，else部分是可选的。关键字“ elif”是“else if”的缩写，有助于避免过多缩进。
 if… elif… … 序列是其他语言中或 语句elif的替代品。switchcase
"""


def fun_if(x):
    if x < 0:
        print("x=0")
    elif x == 0:
        print("x=0")
    elif x == 1:
        print("x=1")
    else:
        print("more")


words = ['cat', 'window', 'of', 'the', 'dog']
for word in words:
    print(word, len(word))

# for 在迭代同一个集合的同时修改该集合的代码可能很难正确执行。相反，循环遍历集合的副本或创建新集合通常更直接
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)
# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)

# range

for i in range(5):
    print(i)

print(list(range(5, 10)))

a = ['Mary', 'had', 'a', 'little', 'lamb']
# 要迭代序列的索引，您可以组合range()和， len()如下所示：
for i in range(len(a)):
    print(1, a[i])

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n // x}")
            break

while True:
    pass


# class MyClass(object):
#     pass

# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

"""
while 和 if 条件句不只可以进行比较，还可以使用任意运算符。

比较运算符 in 和 not in 用于执行确定一个值是否存在（或不存在）于某个容器中的成员检测。 运算符 is 和 is not 用于比较两个对象是否是同一个对象。 所有比较运算符的优先级都一样，且低于任何数值运算符。

比较操作支持链式操作。例如，a < b == c 校验 a 是否小于 b，且 b 是否等于 c。

比较操作可以用布尔运算符 and 和 or 组合，并且，比较操作（或其他布尔运算）的结果都可以用 not 取反。这些操作符的优先级低于比较操作符；not 的优先级最高， or 的优先级最低，因此，A and not B or C 等价于 (A and (not B)) or C。与其他运算符操作一样，此处也可以用圆括号表示想要的组合。

布尔运算符 and 和 or 是所谓的 短路 运算符：其参数从左至右求值，一旦可以确定结果，求值就会停止。例如，如果 A 和 C 为真，B 为假，那么 A and B and C 不会对 C 求值。用作普通值而不是布尔值时，短路运算符的返回值通常是最后一个求了值的参数。

还可以把比较运算或其它布尔表达式的结果赋值给变量，例如：

>>>
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null
'Trondheim'
注意，Python 与 C 不同，在表达式内部赋值必须显式使用 海象运算符 :=。 这避免了 C 程序中常见的问题：要在表达式中写 == 时，却写成了 =。


"""

if __name__ == '__main__':
    fun_if(3)
