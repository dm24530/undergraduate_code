import random

fruits = random.choice(['apple', 'pear', 'banana'])
x = random.sample(range(100), 10)   # sampling without replacement
y= random.random()  # random float
z= random.randrange(6)  # random integer chosen from range(6)
print(fruits)
print(x)
print(y)
print(z)
