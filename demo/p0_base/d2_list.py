

thislist = ["apple", "banana", "cherry"]
blist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(thislist[1])
print(thislist[-1])

#
thislist.append("mantou")
thislist.insert(1,"hello")
print(thislist)

# extend  扩展列表, 添加任何可迭代对象
thislist.extend(blist)
print(thislist)

#copy
mlist = thislist.copy()
nlist = list(thislist)
print(mlist)
print(nlist)
llist = thislist[:]
print(llist)


if __name__ == '__main__':
    pass