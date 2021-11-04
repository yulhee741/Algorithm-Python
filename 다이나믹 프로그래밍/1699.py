# 제곱수의 합
from sys import stdin

n = int(stdin.readline().rstrip())

dp = [i for i in range(n+1)]

for i in range(1, n+1):
    tmp = []
    for j in range(1, i):
        if j*j > i:
            break
        tmp.append(dp[i - j*j])
    if tmp:
        dp[i] = min(tmp) + 1

print(dp[n])

