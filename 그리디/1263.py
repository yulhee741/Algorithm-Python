# 시간 관리
from sys import stdin

n = int(stdin.readline().rstrip())
times = []
for _ in range(n):
    times.append(list(map(int, stdin.readline().split())))

times = sorted(times, key = lambda x : (-x[1]))

start = times[0][1] - times[0][0]

for i in range(1, n):
    if start <= times[i][1]:
        start -= times[i][0]
    else:
        start = times[i][1] - times[i][0]

print(start if start >= 0 else -1)