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

print(team)
for _ in team:
    if _ == 0:
        idx = team.index(_)
        if idx > 0:
            if team[idx-1] == 2:
                team[idx] += 1
                team[idx-1] -= 1
                continue
        if idx < N-1:
            if idx < N-1 and team[idx+1] == 2:
                team[idx] += 1
                team[idx+1] -= 1
                continue

print(team)

print(team.count(0))

