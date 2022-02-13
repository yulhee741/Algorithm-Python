# 아나그램(리스트 해쉬)
from sys import stdin
a = stdin.readline()
b = stdin.readline()
str1 = [0] * 52
str2 = [0] * 52
for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1
    else:
        str[ord(x) - 71] += 1

for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")