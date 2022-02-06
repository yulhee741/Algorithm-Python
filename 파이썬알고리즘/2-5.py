# 수들의 합
from sys import stdin

n, m = map(int, stdin.readline().split())
a = list(map(int, stdin.readline()))
lt = 0
rt = 1
total = a[0]
cnt = 0

while True:
    if total < m:
        if rt < n:
            total += a[rt]
            rt += 1
        else:
            break
    elif total == m:
        cnt += 1
        total -= a[lt]
        lt += 1
    else:
        total -= a[lt]
        lt += 1
print(cnt)