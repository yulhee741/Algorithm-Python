# 과자 나눠주기
from sys import stdin

m, n = map(int, stdin.readline().split())
snacks = list(map(int, stdin.readline().split()))

left = 0
right = max(snacks)
result = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    if mid == 0:
        print(0)
        exit()
        
    for snack in snacks:
        if mid <= snack:
            cnt += snack//mid

    if cnt >= m:
        left = mid + 1
        result = mid
    else:
        right = mid - 1 

print(result)