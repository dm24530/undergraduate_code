from random import choice, random

name = choice('董孙李周赵钱王')
condition = random()
if condition>0.5:          # random()函数返回[0,1)区间上的随机数
    name += choice('付玉延邵子凯')

name += choice('国楠栋涵雪玲瑞')
print(condition)
print(name)
