# 카약과 강풍
import sys

N, S, R = map(int, sys.stdin.readline().split())
#팀의 수, 손상된 팀 수, 카약 더 가져온 팀 수
list_S = list(map(int, sys.stdin.readline().split()))
list_R = list(map(int, sys.stdin.readline().split()))

team = [1 for _ in range(N)]

for s in list_S:
    team[s-1] -= 1

for r in list_R:
    team[r-1] += 1

for i in range(N):
    if team[i] == 0: 
        if i > 0:
            if team[i-1] == 2:
                team[i] += 1
                team[i-1] -= 1
                continue
        if i < N-1:
            if team[i+1] == 2:
                team[i] += 1
                team[i+1] -= 1
                continue

print(team.count(0))

