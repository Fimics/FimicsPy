
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

thistuple1 = ("apple",)
# <class 'tuple'>
print(type(thistuple1))

# NOT a tuple | str
thistuple2 = ("apple")
# <class 'str'>
print(type(thistuple2))

# 一旦创建了元组，就无法更改其值。元组是不可改变的，或也称为不可变的。
# 但有一个解决方法。你可以将元组转换为列表，更改列表，然后将列表转换回元组。

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


if __name__ == '__main__':
    pass