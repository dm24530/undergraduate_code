import jieba

f = open("三国演义.txt", "rb")
txt = f.read()     #读取内容
words = jieba.lcut(txt)    #赋到一个txt对象上，对这个对象进行分词
counts = {}       #定义一个空的字典保存分词结果

for word in words:
    if len(word) == 1:      #排除单个字的分词结果
        continue
    else:
        counts[word] = counts.get(word, 0) + 1     #counts是字典word是字典的键
        
items = list(counts.items())    #把字典的对象列表化
items.sort(key = lambda items: items[1], reverse = True)   #根据词频正向排序
for i in range(20):       #输出前二十个
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
