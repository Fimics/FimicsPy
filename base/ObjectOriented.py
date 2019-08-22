class People(object):
    """
    1.Python中没有像C++中public和private这些关键字来区别公有属性和私有属性
    2.它是以属性命名方式来区分，如果在属性名前面加了2个下划线'__'，则表明该属性是私有属性，
    否则为公有属性（方法也是一样，方法名前面加了2个下划线的话表示该方法是私有的，否则为公有的）
    """

    def __init__(self, name):
        # 私有属性
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, newName):
        if len(newName) >= 5:
            self.__name = newName
        else:
            print("error:名字长度需要大于或者等于5")

    # 析构方法
    # 当对象被删除时，会自动被调用
    # 当有1个变量保存了对象的引用时，此对象的引用计数就会加1
    # 当使用del删除变量指向的对象时，如果对象的引用计数不会1，比如3，那么此时只会让这个引用计数减1，
    # 即变为2，当再次调用del时，变为1，如果再调用1次del，此时会真的把对象进行删除
    def __del__(self):
        print("__del__方法被调用")
        print("%s对象马上被干掉了..." % self.__name)


xiaoming = People("dongGe")
print(xiaoming.getName())
del xiaoming
