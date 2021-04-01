import math
import random
import posixpath as path

print(math.sqrt(16))                  # 计算并输出16的平方根
print(math.cos(math.pi/4))            # 计算余弦值
print(random.choices('abcd', k=8))    # 从字符串'abcd'随机选择8个字符
                                      # 允许重复
print(path.isfile(r'C:\Windows\notepad.exe')) # 测试指定路径是否为文件
