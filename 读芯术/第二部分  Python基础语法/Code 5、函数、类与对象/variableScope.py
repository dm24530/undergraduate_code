# 变量作用域
n=1
def func(a, b):
    global n
    n = b
    c = a*b
    return c
s = func("knock~", 4)
print(s, n)
