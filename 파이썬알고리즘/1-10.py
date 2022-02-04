# 점수 계산
from sys import stdin
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

sum = 0
cnt = 0
for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)