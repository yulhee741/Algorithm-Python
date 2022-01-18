# 이친수
from sys import stdin

N = int(stdin.readline().rstrip())

def solution(n):
    binary_nums = [0, 1]
    if n == 1 or n == 2:
        return 1
    for i in range(2, n+1):
        binary_nums.append(binary_nums[i-1] + binary_nums[i-2])
    return binary_nums[n]

print(solution(N))