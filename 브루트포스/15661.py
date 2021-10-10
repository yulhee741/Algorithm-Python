# 링크와 스타트
from sys import stdin
from itertools import chain, combinations

n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for i in range(n)]
n_list = []
for i in range(1, n+1): 
    n_list.append(i)

combination_list = list(chain.from_iterable(combinations(n_list, r) for r in range(2, n//2 + 1)))
l = len(combination_list)

ans = 100

print(combination_list)

for i in range(l//2+1):
    i, j = combination_list[i]
    k, v = combination_list[l-i-1]

    tmp1 = board[i-1][j-1] + board[j-1][i-1]
    tmp2 = board[k-1][v-1] + board[v-1][k-1]

    ans = min(ans, abs(tmp1-tmp2))

print(ans)
    
