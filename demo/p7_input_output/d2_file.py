import json


def read_text():
    file = open('../../resource/a.txt', 'r')
    text = file.read()
    print(text)


def write_text():
    file = open('../../resource/a.txt', 'w')
    file.write("aaaa")


"""
    在处理文件对象时，最好使用 with 关键字。优点是，子句体结束后，文件会正确关闭，
    即便触发异常也可以。而且，使用 with 相比等效的 try-finally 代码块要简短得多：
"""


def open_file():
    with open('../../resource/a.txt', 'r') as file:
        read_data = file.read()
        print(read_data)
    print(file.closed)


# 使用 json 保存结构化数据
x = [1, 'simple']
print(json.dumps(x))

# dumps() 函数还有一个变体， dump() ，它只将对象序列化为 text file 。因此，如果 f 是 text file 对象，可以这样做：
# json.dump(x, f)

# 要再次解码对象，如果 f 是已打开、供读取的 binary file 或 text file 对象：

# x = json.load(f)


if __name__ == '__main__':
    # read_text()
    # write_text()
    # open_file()
    pass
