# 공유기 설치
from sys import stdin

n, c = map(int, stdin.readline().split())
house = [int(stdin.readline()) for i in range(n)]
house.sort()

left = 1
right = house[-1] - house[0]
result = 0

while left <= right:
    mid = (left + right)//2
    start = house[0]
    cnt = 1

    for i in range(1, n):
        if (start + mid) <= house[i]:
            cnt += 1
            start = house[i]
    if cnt >= c:
        if result < mid:
            result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
