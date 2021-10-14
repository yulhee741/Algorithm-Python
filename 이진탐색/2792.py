# 보석 상자
from sys import stdin

n, m = map(int, stdin.readline().split())
colors = [int(stdin.readline()) for _ in range(m)]

left = 1
right = max(colors)
result = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for color in colors:
        if color % mid == 0:
            cnt += color // mid
        else:
            cnt += color // mid + 1
    
    if cnt <= n:
        right = mid - 1
        result = mid
    else:
        left = mid + 1

print(result)