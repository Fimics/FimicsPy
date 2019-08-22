name = 'abcdef'
print("姓名：%s" % name)

# 字符串切片
print(name[3])
print(name[0:12])
print(name[2:])  # 取下标为2开始到最后的字符
print(name[1:-1])  # 取 下标为1开始 到 最后第2个  之间的字符
print(name[0:6:2])  # 0-6 步长为2
print(name[6:0:-2])

myStr = '  python hello world python  '
sLen = len(myStr)
print(sLen)

# 检测 str 是否包含在 myStr中，如果是返回开始的索引值，否则返回-1
print(myStr.find("python", 0, sLen))
# 跟find()方法一样，只不过如果str不在 myStr中会报一个异常.
print(myStr.index("world", 0, sLen))
# 返回 str在start和end之间 在 myStr里面出现的次数
print(myStr.count("python", 0, sLen))

# 把 myStr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次
print(myStr.replace("python", "java",  myStr.count("python")))

# 以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
print(myStr.split(" ", 2))

# 把字符串的第一个字符大写
print(myStr.capitalize())
print(myStr.lower())
print(myStr.upper())

# 把字符串的每个单词首字母大写
print(myStr.title())

print(myStr.startswith("  python"))
print(myStr.endswith("python  "))

# 删除 myStr 左边的空白字符
print(myStr.lstrip())

# 删除myStr字符串两端的空白字符
print(myStr.strip())

# 如果 myStr 所有字符都是字母 则返回 True,否则返回 False
print(myStr.isalpha())  # myStr.isdigit()

# myStr 中每个字符后面插入str,构造出一个新的字符串
print(myStr.join("cpp"))
