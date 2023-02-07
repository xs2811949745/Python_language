# coding=gbk
name=["a",'b','c']
print(name)
b=[1,2,name]
print(b)
#查
a=name.index("a")
print(a)
#增
name.insert(1,2)
print(name)
name.append("Xye")

print(name)
# 删
del name[2]
print(name)
name.pop(2)
print(name)
# 


