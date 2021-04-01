gen = (2**i for i in range(8))     # 创建生成器对象
print(gen)
print(list(gen))                   # 转换为列表，用完了生成器对象中的所有元素
print(tuple(gen))                  # 转换为元组，得到空元组
gen = (2**i for i in range(8))     # 重新创建生成器对象
print(next(gen))                   # 使用next()函数访问下一个元素
print(next(gen))
for item in gen:                   # 使用for循环访问剩余的所有元素
    print(item, end=' ')
