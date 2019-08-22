'''
定义类
定义类时有2种：新式类和经典类，上面的Car为经典类，如果是Car(object)则为新式类
类名 的命名规则按照"大驼峰"
'''


# 定义类
class Car:

    # 初始化函数，用来完成一些默认的设定
    def __init__(self):
        self.color = "red"
        self.wheelNum = 9

    """
    1.__init__()方法，在创建一个对象时默认被调用，不需要手动调用
    2.__init__(self)中，默认有1个参数名字为self，如果在创建对象时传递了2个实参，
    那么__init__(self)中出了self作为第一个形参外还需要2个形参，例如__init__(self,x,y)
    3.__init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递进去
    """

    def __init__(self, newWheelNum, newColor):
        self.wheelNum = newWheelNum
        self.color = newColor

    """
    1.在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
    2. 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
    """

    def __str__(self):
        msg = "嘿。。。我的颜色是" + self.color + "我有" + str(self.wheelNum) + "个轮胎..."
        return msg

    # 移动
    def move(self):
        print('车在奔跑...')

    # 鸣笛
    def toot(self):
        print("车在鸣笛...嘟嘟..")


# car = Car()
car = Car(3, "blue")
car.move()
car.toot()
"""
当创建Car对象后，在没有调用__init__()方法的前提下，
BMW就默认拥有了2个属性wheelNum和color，原因是__init__()方法是在创建对象后，就立刻被默认调用了
"""
print(car.color)
print(car.wheelNum)
# 动态给对象添加属性
car.color = "black"
car.wheelNum = 4

print(car.color)
print(car.wheelNum)

car1 = Car(2, "yellow")
print(car1.color)
print(car1.wheelNum)
print(car)
