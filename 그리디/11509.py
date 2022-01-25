# 풍선 맞추기
from sys import stdin

n = int(stdin.readline().rstrip())
h = list(map(int, stdin.readline().split()))
arrow = [0 for i in range(1000001)]

for i in h:
    if arrow[i] > 0:
        arrow[i]-=1
        arrow[i - 1] += 1
    else:
        arrow[i - 1] += 1

print(sum(arrow))