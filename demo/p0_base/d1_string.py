
# 字符串是数组
a = " Hello ,World "
print(a)
print(a[1])
print(len(a))
print("a" in a)
print("x" not in a)
# 遍历
# for i in a:
#     print(i)

# 切片
# 获取位置 2 到位置 5 的字符（不包括）
print(a[2:5])
# 获取从起始到位置 5 的字符（不包括）
print(a[:5])
print(a[5:])

# 使用负索引从字符串末尾开始切片
print(a[-5:-2])

# 修改
print(a.lower())

# 链式调用（Chain of Responsibility） 或 命令模式（Command Pattern）
print(a.strip())
print(a.replace("H","W"))
print(a.split(",")) # returns ['Hello', ' World!']

if __name__ == '__main__':
    pass