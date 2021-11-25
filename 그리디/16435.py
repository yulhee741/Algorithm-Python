# 스네이크버드
from sys import stdin

n, l = map(int, stdin.readline().split())
fruit = list(map(int, stdin.readline().split()))

fruit.sort()
result = l
for h in fruit:
    if h <= result:
        result += 1
    elif h > result:
        break

print(result)
    