digits = range(10)
for i in digits:               # 选择一个数字
    if i==0:
        continue                # 第一位数不能是0
    for j in digits:
        if j==i:
            continue            # 第2位与第1位相同，则忽略后面的操作
        for k in digits:
            if k in (i,j):
                continue        # 3位数字必须互不相同
            print(int(str(i)+str(j)+str(k)), end= ' ')
