lst = [1, 2, 3, 4, 5, 6]
print(lst.pop())            # 删除并返回最后一个元素
print(lst)
print(lst.pop(0))           # 删除并返回下标为0的元素，后面的元素向前移动
print(lst)
print(lst.pop(2))           # 删除并返回下标为2的元素，后面的元素向前移动
print(lst)
lst = [1, 2, 3, 2, 4, 2]
lst.remove(2)               # 删除第一个2，该方法没有返回值
print(lst)
