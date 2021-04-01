data = {30, 40, 50}
data.add(20)               # 增加新元素20
print(data)
data.add(50)               # 集合中已包含50，忽略本次操作
print(data)
data.update({40, 60})      # 忽略40，增加新元素60
print(data)

data = {30, 40, 50}
data.remove(30)          # 删除元素30
print(data)
data.discard(30)         # 集合中没有30，忽略本次操作
print(data.pop())        # 删除并返回集合中的一个元素
print(data)

