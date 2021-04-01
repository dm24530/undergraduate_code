a = 20
b = 20
 
if ( a is b ):
   print ("1 : a 和 b 有相同的标识")
else:
   print ("1 :  a 和 b 没有相同的标识")

print(id(a))
print(id(b))


# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 : a 和 b 有相同的标识")
else:
   print ("3 : a 和 b 没有相同的标识")
 
# is 与 == 的区别
a = [1, 2, 3]
b = [1, 2, 3]
print(b == a)
print(b is a)

print(id(a))
print(id(b))