# 입국심사
from sys import stdin

n, m = map(int, stdin.readline().split())
time = []

for i in range(n):
    t = int(stdin.readline())
    time.append(t)

left = min(time)
right = max(time) * m
result = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for t in time:
        cnt += (mid//t)

    if cnt >= m:
        right = mid - 1
        result = mid
    else:
        left = mid + 1

print(result)