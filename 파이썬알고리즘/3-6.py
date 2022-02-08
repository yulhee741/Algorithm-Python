# 씨름 선수(그리디)
from sys import stdin
n = int(stdin.readline())
body = []
for i in range(n):
    a, b = map(int, stdin.readline().split())
    body.append((a,b))
body.sort(reverse=True)

largest = 0
cnt = 0
for x, y in body:
    if y > largest:
        largest = y
        cnt += 1

print(cnt)
