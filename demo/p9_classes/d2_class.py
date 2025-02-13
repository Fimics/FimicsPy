import this


class Person:
    def __init__(self, name):
        self.name = name


class Person2(object):
    i = 12345

    def __init__(self):
        self.i = 5153125312
        self.data = [1, 2, 3]

    def f(self):
        print(self.i)
        return "hello world"


person = Person("jack")
person.age = 20
print(person.age)
print(person.name)

p2 = Person2()
print(p2.f())
print(len(p2.data))

print("-----------------")


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r)
print(x.i)


class Dog:
    # 类变量被所有实例所共享
    kind = 'canine'
    # 共享数据可能在涉及 mutable 对象例如列表和字典的时候导致令人惊讶的结果。
    # 例如以下代码中的 tricks 列表不应该被用作类变量，因为所有的 Dog 实例将只共享一个单独的列表:
    tricks = []  # 类变量的错误用法

    # 实例变量为每个实例所独有
    def __init__(self, name):
        self.name = name


d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)


# 正确的类设计应该使用实例变量:
class Dog1:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


print("------------")
d = Dog1('Fido')
e = Dog1('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)


# 在类之外定义的函数
def f1(self, x, y):
    return min(x, x + y)


if __name__ == '__main__':
    pass
