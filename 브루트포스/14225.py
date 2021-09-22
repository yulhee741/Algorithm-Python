# 부분 수열의 합
from sys import stdin
from itertools import chain, combinations

n = int(stdin.readline().rstrip())
s_list = list(map(int, stdin.readline().split()))

sum_list = []
combination_list = list(chain.from_iterable(combinations(s_list, r) for r in range(1, n + 1)))

for num in combination_list:
    sum_list.append(sum(num))

check = 1
sum_list = sorted(set(sum_list))

for n in sum_list:
    if n != check:
        print(check)
        exit()
    else:
        check += 1

print(sum_list[-1] + 1)