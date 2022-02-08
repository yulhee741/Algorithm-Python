# 회의실 배정(그리디)
from sys import stdin

n = int(stdin.readline())
meeting = []
for i in range(n):
    s, e = map(int, stdin.readline().split())
    meeting.append((s,e))

meeting.sort(key=lambda x: (x[1], x[0]))
et = 0
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1

print(cnt)
