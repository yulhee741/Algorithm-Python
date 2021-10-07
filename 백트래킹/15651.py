# N과 M (3)
from sys import stdin
from itertools import product

n, m = map(int, stdin.readline().split())
nums = []

for i in range(n):
    nums.append(i+1)

results = set(product(nums, repeat = m))
ans = []

for result in results:
    ans.append(result)

ans.sort()
for a in ans:
    print(*a)