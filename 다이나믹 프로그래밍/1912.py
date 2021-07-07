# 연속합
from sys import stdin

n = int(stdin.readline().rstrip())
n_arr = list(map(int, stdin.readline().split()))

dp = [0] * n

for i in range(n):
    dp[i] = max(n_arr[i], dp[i-1]+n_arr[i])

print(max(dp))