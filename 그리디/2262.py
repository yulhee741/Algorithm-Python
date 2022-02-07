# 토너먼트 만들기
from sys import stdin

n = int(stdin.readline())
tournament = list(map(int, stdin.readline().split()))
rank = sorted(tournament, reverse=True)
res = 0
for i in rank[:-1]:
    idx = tournament.index(i)
    if idx == 0:
        res += i - tournament[idx+1]
    elif idx == len(tournament)-1:
        res += i - tournament[idx-1]
    else:
        tmp = min(i - tournament[idx+1], i - tournament[idx-1])
        res += tmp
    tournament.pop(idx)

print(res)