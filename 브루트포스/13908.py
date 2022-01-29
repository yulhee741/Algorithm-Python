# 비밀번호

from sys import stdin
from itertools import permutations

n, m = map(int, stdin.readline().split())
need_nums = list(map(int, stdin.readline().split())) if m != 0 else []

def is_valid(password):
    return all(map(lambda num: num in password, need_nums))

def solve(password):
    if len(password) == n:
        return 1 if is_valid(password) else 0

    result = 0
    for i in range(10):
        password.append(i)
        result += solve(password)
        password.pop()

    return result

print(solve([]))
