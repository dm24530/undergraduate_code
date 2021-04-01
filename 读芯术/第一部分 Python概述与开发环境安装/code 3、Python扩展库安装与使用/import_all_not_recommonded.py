from itertools import *

characters = '1234'
for item in combinations(characters, 3):  # 从4个字符中任选3个的组合
    print(item, end=' ')                  # end=' '表示输出后不换行
#    print(type(item))
print('\n'+'='*20)                        # 行号后输出20个等于号
for item in permutations(characters, 3):  # 从4个字符中任选3个的排列
    print(item, end=' ')
