# 회의실 배정
from sys import stdin

n = int(stdin.readline().rstrip())
meeting = []

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    meeting.append((a,b))
 
meeting.sort() 
meeting.sort(key=lambda x:x[1])

start, end = meeting[0]
cnt = 1

for s, e in meeting[1:]:
    if end <= s:
        cnt += 1
        end = e

print(cnt)


