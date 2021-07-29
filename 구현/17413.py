# 단어 뒤집기 2
from sys import stdin

s = stdin.readline().rstrip()
flag = False
word = ""
answer = ""

for i in range(len(s)):
    if s[i] == "<":
        flag = True
        while s[i] != ">":
            word += s[i]
            i += 1
    elif s[i] == " " and flag == False:
        word += s[i]
        answer += word
        word = ""
    elif s[i] == ">" and flag == True:
        word += s[i]
        answer += word
        word, flag = "", False
    elif flag == False:
        word = s[i] + word


print(answer + word)
        