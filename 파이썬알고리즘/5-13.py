# 라이브러리를 이용한 조합(수들의 조합)
from sys import stdin
import itertools as it

n, k = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
cnt = 0
for x in it.combinations(a, k):
    if sum(x) % m == 0:
        cnt += 1
print(cnt)