# 게임을 만든 동준이
from sys import stdin

n = int(stdin.readline().rstrip())
score = [int(stdin.readline()) for _ in range(n)]

cnt = 0
for i in range(n-1, 0, -1):
    if score[i] <= score[i-1]:
        tmp = score[i-1] - score[i] + 1
        score[i-1] -= tmp
        cnt += tmp

print(cnt)