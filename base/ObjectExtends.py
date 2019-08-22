# 定义一个父类，如下:
class Cat(object):

    def __init__(self, name, color="白色"):
        self.name = name
        self.color = color

    def run(self):
        print("%s--在跑" % self.name)


# 定义一个子类，继承Cat类如下:
class Bosi(Cat):

    def setNewName(self, newName):
        self.name = newName

    def eat(self):
        print("%s--在吃" % self.name)


bs = Bosi("印度猫")
print('bs的名字为:%s' % bs.name)
print('bs的颜色为:%s' % bs.color)
bs.eat()
bs.setNewName('波斯')
bs.run()


class base(object):
    def test(self):
        print('----base test----')


class A(base):
    def test(self):
        print('----A test----')


# 定义一个父类
class B(base):
    def test(self):
        print('----B test----')


# 定义一个子类，继承自A、B
class C(A, B):
    pass


obj_C = C()
obj_C.test()

print(C.__mro__)  # 可以查看C类的对象搜索方法时的先后顺序


class Cat(object):
    def __init__(self, name):
        self.name = name
        self.color = 'yellow'


class Bosi(Cat):
    """
    调用父类方法
    """

    def __init__(self, name):
        # 调用父类的__init__方法1(python2)
        # Cat.__init__(self,name)
        # 调用父类的__init__方法2
        # super(Bosi,self).__init__(name)
        # 调用父类的__init__方法3
        super().__init__(name)

    def getName(self):
        return self.name


bosi = Bosi('xiaohua')

print(bosi.name)
print(bosi.color)


# Python “鸭子类型”
class F1(object):
    def show(self):
        print('F1.show')


class S1(F1):

    def show(self):
        print('S1.show')


class S2(F1):

    def show(self):
        print('S2.show')


def Func(obj):
    print(obj.show())

s1_obj = S1()
Func(s1_obj)

s2_obj = S2()
Func(s2_obj)
