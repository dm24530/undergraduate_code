# 字符串遍历
str1="hello,world"
for p in str1:
    print(p)


print("Hello\nWorld\n\nGoodbye\t\t32\n")       #转义字符

# 字符串操作
text = '处处飞花飞处处；声声笑语笑声声。'
print(text.rindex('处'))
print(text.index('声'))
print(text.count('处'))

text = "Python是一门非常棒的编程语言。"
# replace()方法返回替换后的新字符串，可以直接再次调用replace()方法
print(text.replace('棒','优雅').replace('编程', '程序设计'))
print(text)

table = ''.maketrans('0123456789', '零一二三四伍陆柒捌玖')
print('Tel:62819743'.translate(table))

print('居左'.ljust(20)+'结束')
print('居右'.rjust(20, '#'))        # 左侧使用井号填充
print('居中'.center(20, '='))       # 两侧使用等号填充

text = 'Beautiful is better than ugly.'
print(text.split())                     # 使用空白字符进行分隔
print(text.split(maxsplit=1))           # 最多分隔一次
print(text.rsplit(maxsplit=2))          # 最多分隔两次
print('1,2,3,4'.split(','))             # 使用逗号作为分隔符
print(','.join(['1', '2', '3', '4']))   # 使用逗号作为连接符
print(':'.join(map(str, range(1, 5))))  # 使用冒号作为连接符
print(''.join(map(str, range(1, 5))))   # 直接连接，不插入任何连接符

text = 'Simple is better than complex.'
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.title())
print(text.swapcase())

text = '   ======test===#####   '
print(text.strip())          # 删除两侧的空白字符
print(text.strip('=# '))     # 删除两侧的=、#和空格

