info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '地球亚洲中国北京'}
print(info)
print(info["name"])
print(info.get("age"))
info["id"] = 200;
print(info)

info["age"] = 20;
print(info)

# 删除元素
del info["age"]
print(info)
# info.clear()
# print(info)


print(len(info))
print(info.keys())
print(info.values())
print(info.items())

for key in info.keys():
    print(key)
    print(info.get(key))

for value in info.values():
    print(value)

for item in info.items():
    print(item)

for key, value in info.items():
    print("key=%s,value=%s" % (key, value))

chars = ['a', 'b', 'c', 'd']
for i, chr in enumerate(chars):
    print (i, chr)
