class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        print('Hello, my name is {} and my age is {}'.format(self.name, self.age))

    def __str__(self):
        return f'{self.name} {self.age}'


p1 = Person("John", 36)
# p1.age=90

print(p1.name)
print(p1.age)
print(p1)
print(p1.myfun())

# 删除属性
# del p1.age
# print(p1)

# 删除对象
del p1

if __name__ == '__main__':
    pass
