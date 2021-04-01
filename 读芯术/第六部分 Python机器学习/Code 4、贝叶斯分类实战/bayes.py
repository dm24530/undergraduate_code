from re import sub      #正则表达式中sub替换功能， 主要是用来删除邮件中的标点符号等无意义字符
#from os import listdir  #用于返回指定的文件夹包含的文件列表,邮件放在文件夹内
from collections import Counter  #计算功能，计算出现次数最多的词时用到
from itertools import chain   #迭代器，可依次返回可迭代对象的元素
from numpy import array
from jieba import cut
from sklearn.naive_bayes import MultinomialNB  #先验为多项式分布的朴素贝叶斯


#处理每个垃圾邮件中的词语
def getWordsFromFile(txtFile):
    # 获取每一封邮件中的所有词语
    words = []
    # 所有存储邮件文本内容的记事本文件都使用UTF8编码
    with open(txtFile, encoding='utf8') as fp:
        for line in fp:
            # 遍历每一行，删除两端的空白字符
            line = line.strip()
            # 过滤干扰字符或无效字符
            line = sub(r'[.【】0-9、—。，！~\*]', '', line)
            # 分词
            line = cut(line)
            # 过滤长度为1的词
            line = filter(lambda word: len(word)>1, line)
            # 把本行文本预处理得到的词语添加到words列表中
            words.extend(line)
    # 返回包含当前邮件文本中所有有效词语的列表
    return words

# 存放所有文件中的单词
# 每个元素是一个子列表，其中存放一个文件中的所有单词
allWords = []

#获取全部训练集中出现次数前n多的词
def getTopNWords(topN):
    # 按文件编号顺序处理当前文件夹中所有记事本文件
    # 训练集中共151封邮件内容，0.txt到126.txt是垃圾邮件内容
    # 127.txt到150.txt为正常邮件内容
    txtFiles = [str(i)+'.txt' for i in range(151)]  #遍历所有的训练集
    # 获取训练集中所有邮件中的全部单词
    for txtFile in txtFiles:
        allWords.append(getWordsFromFile(txtFile))
    # 获取并返回出现次数最多的前topN个单词
    freq = Counter(chain(*allWords))
    return [w[0] for w in freq.most_common(topN)]

# 全部训练集中出现次数最多的前600个单词
topWords = getTopNWords(600)

# 获取特征向量，前600个单词的每个单词在每个邮件中出现的频率
vectors = []
for words in allWords:
    temp = list(map(lambda x: words.count(x), topWords))
    vectors.append(temp)
vectors = array(vectors)
# 训练集中每个邮件的标签，1表示垃圾邮件，0表示正常邮件
labels = array([1]*127 + [0]*24)

# 创建模型，使用已知训练集进行训练
model = MultinomialNB()
model.fit(vectors, labels)

def predict(txtFile):
    # 获取指定邮件文件内容，返回分类结果
    words = getWordsFromFile(txtFile)
    currentVector = array(tuple(map(lambda x: words.count(x),
                                    topWords)))
    result = model.predict(currentVector.reshape(1, -1))[0]
    return '垃圾邮件' if result==1 else '正常邮件'

# 151.txt至155.txt为测试邮件内容
for mail in ('%d.txt'%i for i in range(151, 157)):
    print(mail, predict(mail), sep=':')
