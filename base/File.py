import os

f = open("../resource/a.txt", 'r+')
print(f.read(2))
f.seek(0)
f.close()

aFile = open('../resource/a.txt', 'r+')
# aFile.write("new word")

# print(aFile.read())
# f.seek(0)


lines = aFile.readlines()
i = 1
for line in lines:
    print(i, line)
    i += 1

aFile.close()

bFile = open("../resource/b.txt", "r")
str = bFile.read(3)
print(str)
# 查找当前位置
position = bFile.tell()
print(position)

"""
seek(offset, from)有2个参数

offset:偏移量
from:方向
0:表示文件开头
1:表示当前位置
2:表示文件末尾
"""

# os.rename("../resource/c.txt", "../resource/cc.txt")
# os.remove("../resource/d.txt")

# os.mkdir("../resource/asset")
print(os.getcwd())
print(os.listdir("../"))
os.rmdir("../resource/asset")

