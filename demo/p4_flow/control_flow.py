"""
可以有零个或多个elif部分，else部分是可选的。关键字“ elif”是“else if”的缩写，有助于避免过多缩进。
 if… elif… … 序列是其他语言中或 语句elif的替代品。switchcase
"""


def fun_if(x):
    if x < 0:
        print("x=0")
    elif x == 0:
        print("x=0")
    elif x == 1:
        print("x=1")
    else:
        print("more")


words = ['cat', 'window', 'of', 'the', 'dog']
for word in words:
    print(word, len(word))


# for 在迭代同一个集合的同时修改该集合的代码可能很难正确执行。相反，循环遍历集合的副本或创建新集合通常更直接
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)
# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)

# range

for i in range(5):
    print(i)

print(list(range(5,10)))

a = ['Mary', 'had', 'a', 'little', 'lamb']
# 要迭代序列的索引，您可以组合range()和， len()如下所示：
for i in range(len(a)):
    print(1,a[i])


if __name__ == '__main__':
    fun_if(3)
