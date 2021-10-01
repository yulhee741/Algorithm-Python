# 용돈 관리
from sys import stdin

n, m = map(int, stdin.readline().split())
coin_list = [int(stdin.readline()) for i in range(n)]

left = max(coin_list)
right = sum(coin_list)
result = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 1
    money = mid

    for coin in coin_list:
        if coin <= money:
            money -= coin
        else:
            money = mid
            cnt += 1
            money -= coin

    if cnt > m: # 기준 돈이 작은 경우
        left = mid + 1
    else:
        right = mid - 1
        result = mid

print(result)