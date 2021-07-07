# 동전
from sys import stdin

# 동전 종류 수, 목표 금액
n, k = map(int, stdin.readline().split())
coin = [int(stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
# i원짜리 동전 하나로 i원을 만드는 경우의 수 = 1
dp[0] = 1

for i in coin:
    for j in range(i, k + 1):
        if j - i >= 0:
            dp[j] += dp[j-i]
print(dp[k])