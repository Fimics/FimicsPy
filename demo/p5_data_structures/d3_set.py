# 集合是由不重复元素组成的无序容器。基本用法包括成员检测、消除重复元素。集合对象支持合集、交集、差集、对称差分等数学运算。
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print("orange" in basket)

a = set('abracadabra')
b = set('alacazam')

# 存在于 a 中但不存在于 b 中的字母
print(a-b)
# 存在于 a 或 b 中或两者中皆有的字母
print(a|b)
# 同时存在于 a 和 b 中的字母
print(a&b)

# 在于 a 或 b 中但非两者中皆有的字母
print(a^b)


print(a)
print(b)

if __name__ == '__main__':
    pass