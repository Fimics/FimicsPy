# 类属性
class People(object):
    name = 'Tom'  # 公有的类属性
    __age = 12  # 私有的类属性


p = People()

print(p.name)  # 正确
print(People.name)  # 正确


# print(p.__age)  # 错误，不能在类外通过实例对象访问私有的类属性
# print(People.__age)  # 错误，不能在类外通过类对象访问私有的类属性


class People(object):
    address = '山东'  # 类属性

    def __init__(self):
        self.name = 'xiaowang'  # 实例属性
        self.age = 20  # 实例属性


# 实例属性(对象属性)
p = People()
p.age = 12  # 实例属性
print(p.address)  # 正确
print(p.name)  # 正确
print(p.age)  # 正确

print(People.address)  # 正确


# print(People.name)  # 错误
# print(People.age)  # 错误


# 通过实例(对象)去修改类属性

class People(object):
    country = 'china'  # 类属性


print(People.country)
p = People()
print(p.country)
p.country = 'japan'
print(p.country)  # 实例属性会屏蔽掉同名的类属性
print(People.country)
del p.country  # 删除实例属性
print(p.country)


"""
如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。如果通过实例对象去引用
，会产生一个同名的实例属性，这种方式修改的是实例属性，不会影响到类属性，
并且之后如果通过实例对象去引用该名称的属性，实例属性会强制屏蔽掉类属性，即引用的是实例属性，除非删除了该实例属性。
"""