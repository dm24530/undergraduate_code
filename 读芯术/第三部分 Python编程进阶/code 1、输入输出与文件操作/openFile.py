textFile = open('file.txt', 'rt')
print(textFile.readline())
textFile.close()

binFile = open('file.txt', 'rb')
print(binFile.readline())
binFile.close()
