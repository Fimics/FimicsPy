class Animal(object):
    age = 10

    def __init__(self, name, address):
        self.name = name
        self.address = 'beijing'
        print(f"my name is {self.name} and my address is {self.address}")

    def bark(self):
        print("animal")


class Dog(Animal):
    def __init__(self, name, address):
        super(Dog, self).__init__(name, address)

    def bark(self):
        print("dog")


dog = Dog('beijing', 'beijing')
print(dog.name)
print(dog.age)

if isinstance(dog, Animal):
    print("dog is an Animal")

if issubclass(Dog, Animal):
    print("Dog is an Animal")


class XDog(Dog, Animal):

    def __init__(self, name, address):
        super(XDog, self).__init__(name, address)




print("------------------")
xdog = XDog('beijing', 'beijing')
print(xdog.bark())

# 多继承

"""
对于多数目的来说，在最简单的情况下，你可以认为搜索从父类所继承属性的操作是深度优先、从左到右的，
当层次结构存在重叠时不会在同一个类中搜索两次。 因此，如果某个属性在 DerivedClassName 中找不到
，就会在 Base1 中搜索它，然后（递归地）在 Base1 的基类中搜索，如果在那里也找不到，就将在 Base2 中搜索，依此类推。

真实情况比这个更复杂一些；方法解析顺序会动态改变以支持对 super() 的协同调用。 这种方式在某些其他多重继承
型语言中被称为后续方法调用，它比单继承型语言中的 super 调用更强大。
"""
# class DerivedClassName(Base1, Base2, Base3):
#     pass

if __name__ == '__main__':
    pass
