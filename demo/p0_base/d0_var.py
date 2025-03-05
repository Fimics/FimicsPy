import random

# 变量

# 变量不需要用任何特定类型声明，甚至可以在设置后改变类型
x =4
x ="steven"
print(x)

# 如果您想指定变量的数据类型，可以通过强制转换来完成
# x = str(3)
# y = int(3)
# z = float(3)
#
# print(f"x ={x}  y ={y}  z={z}")
# print(type(x))
# print(type(y))
# print(type(z))

# 多个值对应多个变量
'''x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)'''

#
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)
print(x+y+z)



if __name__ == '__main__':
    print(random.randrange(0,11,5))
    pass