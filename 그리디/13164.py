# 행복 유치원
from sys import stdin

n, k = map(int, stdin.readline().rstrip().split())
height = list(map(int, stdin.readline().rstrip().split()))

sub_height = []

for i in range(n-1):
    sub_height.append(height[i+1] - height[i])

sub_height.sort()

print(sum(sub_height[:n-k]))