# 使用列表函数反转字符串
def reverseStr(s):
    ls = list(s)
    ls.reverse()
    s ="".join(ls)
    print(s)
    
str = "sdfadfw8r873r323230"
reverseStr(str)
