import math

year = 2016
event = 'Referendum'

# 使用 格式化字符串字面值 ，要在字符串开头的引号/三引号前添加 f 或 F 。在这种字符串中，可以在 { 和 } 字符之间输入引用的变量
print(f'{year} {event}')

yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
a ='{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
print(a)

s = 'Hello, world.'
print(s)
print(str(s))
print(repr(s))
print(str(1/7))

print(f'The value of pi is approximately {math.pi:.3f}.')

# 在 ':' 后传递整数，为该字段设置最小字符宽度，常用于列对齐
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

# format 方法
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

# 位置参数和关键字参数可以任意组合：
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))
# 如果不想分拆较长的格式字符串，最好按名称引用变量进行格式化，不要按位置。这项操作可以通过传递字典，并用方括号 '[]' 访问键来完成
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

# 与内置函数 vars() 一同使用时这种方式非常实用，它将返回一个包含所有局部变量的字典:
table = {k: str(v) for k, v in vars().items()}
message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
print(message.format(**table))

if __name__ == '__main__':
    pass