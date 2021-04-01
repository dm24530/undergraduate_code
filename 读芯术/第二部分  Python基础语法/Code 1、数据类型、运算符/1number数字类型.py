import math

print(math.factorial(32))               # 计算32的阶乘
print(0.4-0.3 == 0.1)                   # 实数之间尽量避免直接比较大小

print(math.isclose(0.4-0.3, 0.1))       # 测试两个实数是否足够接近

a = 6**0.5

print(6**0.5**2 == 6)

c = 3+4j                                # Python内置支持复数及其运算
print(c+c)                              # 复数相加
print(c.real)                           # 查看复数的实部
print(c.imag)                           # 查看复数的虚部
print(3+4j.imag)                        # 相当于3+(4j).imag
