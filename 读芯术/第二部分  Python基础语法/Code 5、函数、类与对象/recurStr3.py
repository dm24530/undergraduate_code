# 用递归进行字符串反转
def reverseRecu(s):
    if len(s) <= 0:
        return ""
    else:
        return reverseRecu(s[1:]) + s[0]

str = "sdfadfw8r873r30"
print(reverseRecu(str))
