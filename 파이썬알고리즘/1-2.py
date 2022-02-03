# K번째 수
from sys import stdin

T = int(stdin.readline())

for t in range(T):
    n, s, e, k = map(int, stdin.readline().split())
    nums = list(map(int, stdin.readline().split()))
    nums = nums[s-1:e]
    nums.sort()
    print("#%d %d" %(t+1, nums[k-1]))