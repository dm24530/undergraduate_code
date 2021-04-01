from math import pi as PI
from os.path import getsize
from random import choice

r = 3
print(round(PI*r*r, 2))                      # 计算半径为3的圆面积
print(getsize(r'C:\Windows\notepad.exe'))    # 计算文件大小，单位为字节
print(choice('Python'))                      # 从字符串中随机选择一个字符
