# 라이브러리 이용한 순열(수열추측하기)
from sys import stdin
import itertools as it

n, f = map(int, stdin.readline().split())
b = [1] * n
for i in range(1, n):
    b[i] = b[i-1] * (n-i)//i
a=list(range(1, n+1))
for tmp in it.permutations(a):
    sum_n = 0
    for l, x in enumerate(tmp):
        sum_n += (x * b[l])
    if sum_n == f:
        for x in tmp:
            print(x, end=' ')
        break