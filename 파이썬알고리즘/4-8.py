# 단어찾기(해쉬)
from sys import stdin
n = int(stdin.readline())
p = dict()

for i in range(n):
    word = stdin.readline()
    p[word] = 1

for i in range(n-1):
    word = stdin.readline()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break