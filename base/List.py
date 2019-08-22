namesList = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
namesList1 = ["java", "python"]
# 比C语言的数组强大的地方在于列表中的元素可以是不同类型的
testList = [1, 'a']

print(namesList[0])

namesList.append("daWang")
# 通过extend可以将另一个集合中的元素逐一添加到列表中
namesList.extend(namesList1)

for name in namesList:
    print(name)

length = len(namesList)
i = 0;
while i < length:
    print(namesList[i])
    i += 1

a = [0, 1, 2]
a.insert(1, 3)
print(a)

# update item
a[2] = 30
print(a)

# 查找元素("查"in, not in, index, count)
print(3 in a)
print(22 not in a)
print(a.index(2))
# print(a.index(2, 0, 2))
print(a.count(1))

# 删除元素("删"del, pop, remove)
'''
del：根据下标进行删除
pop：删除最后一个元素
remove：根据元素的值进行删除
'''
movieName = ['加勒比海盗', '骇客帝国', '第一滴血', '指环王', '霍比特人', '速度与激情']

print(movieName)
del movieName[0]
print(movieName)
movieName.pop()
print(movieName)
movieName.remove(movieName[2])
print(movieName)

"""
排序(sort, reverse)
1.sort方法是将list按特定顺序重新排列，默认为由小到大，参数reverse=True可改为倒序，由大到小
"""

b = [1, 4, 2, 3]
b.sort()
print(b)
b.sort(reverse=True)
print(b)

# 列表的嵌套

schoolNames = [['北京大学', '清华大学'],
               ['南开大学', '天津大学', '天津师范大学'],
               ['山东大学', '中国海洋大学']]

for names in schoolNames:
    for name in names:
        print(name)



