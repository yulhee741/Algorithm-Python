# 아나그램(딕셔너리 해쉬)
from sys import stdin
a = stdin.readline()
b = stdin.readline()
str1 = dict()

for x in a:
    str1[x] = str1.get(x, 0) + 1

for x in b:
    str1[x] = str1.get(x, 0) - 1

for x in a:
    if str1.get(x) > 0:
        print("NO")
        break
else:
    print("YES")
