from collections import deque


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))  # 从 4 号位开始查找下一个 banana
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)

# 列表方法使得将列表用作栈非常容易，最后添加的元素会最先被取出（“后进先出”）。 要将一个条目添加到栈顶，可使用 append()。 要从栈顶取出一个条目，则使用 pop() 且不必显式指定索引
print("---------")
stack = [3, 4, 5 ]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)

# 列表也可以用作队列，最先加入的元素，最先取出（“先进先出”）；然而，列表作为队列的效率很低。因为，在列表末尾添加和删除元素非常快，但在列表开头插入或移除元素却很慢（因为所有其他元素都必须移动一位）
print("----------")

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry 到了
queue.append("Graham")          # Graham 到了
print(queue)
queue.popleft()                 # 第一个到的现在走了
print(queue)


# 列表推导式创建列表的方式更简洁。常见的用法为，对序列或可迭代对象中的每个元素应用某种操作，用生成的结果创建新的列表；或用满足特定条件的元素创建子序列。
print("---------")
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)
# 注意，这段代码创建（或覆盖）变量 x，该变量在循环结束后仍然存在。下述方法可以无副作用地计算平方列表：
squares1 = list(map(lambda x: x**2, range(10)))
# squares = [x**2 for x in range(10)]
print(squares1)

# 列表推导式的方括号内包含以下内容：一个表达式，后面为一个 for 子句，然后，是零个或多个 for 或 if 子句。
# 结果是由表达式依据 for 和 if 子句求值计算而得出一个新列表。 举例来说，以下列表推导式将两个列表中不相等的元素组合起来
# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# 表达式是元组（例如上例的 (x, y)）时，必须加上括号：
# [(x, x**2) for x in range(6)]

# del 语句
"""
可以按索引而不是按值从一个列表移除条目：即使用 del 语句。 这不同于返回一个值的 pop() 方法。
del 语句还可被用来从列表移除切片或清空整个列表（之前我们通过将一个空列表赋值给切片实现此功能）。 例如:
"""

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)

if __name__ == '__main__':
   pass