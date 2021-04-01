from random import sample

# 在range(10000)中任选10个不重复的随机数
data = sample(range(10000), 10)
print(data)
data.reverse()             # 翻转，首尾交换，该方法没有返回值
print(data)
data.sort()                # 按元素大小进行排序，该方法没有返回值
print(data)
data.sort(key=str)         # 按所有元素转换为字符串后的大小进行排序
print(data)
