# 创建列表对象
x_list = [1, 2, 3]
# 创建元组对象
x_tuple = (1, 2, 3)
# 创建字典对象，元素形式为“键:值”
x_dict = {'a':97, 'b':98, 'c':99}
# 创建集合对象
x_set = {1, 2, 3}
# 使用下标访问列表中指定位置的元素，元素下标从0开始
print(x_list[1])
# 元组也支持使用序号作为下标，1表示第二个元素的下标
print(x_tuple[1])
# 访问字典中特定“键”对应的“值”，字典对象的下标是“键”
print(x_dict['a'])
# 查看列表长度，也就是其中元素的个数
print(len(x_list))
# 查看元素2在元组中首次出现的位置
print(x_tuple.index(2))
# 查看字典中哪些“键”对应的“值”为98
for key, value in x_dict.items():
    if value == 98:
        print(key)
# 查看集合中元素的最大值
print(max(x_set))
