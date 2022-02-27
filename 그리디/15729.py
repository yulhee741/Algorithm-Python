# 방탈출
from sys import stdin

n = int(stdin.readline())

def bool_change(a):
    if a == '0':
        return False
    elif a == '1':
        return True

button = list(map(bool_change, stdin.readline().split()))
now = [False for _ in range(n)]
cnt = 0

for i in range(n):
    if now[i] != button[i]:
        now[i] = not now[i]
        cnt += 1
        if i + 1 < n:
            now[i+1] = not now[i+1]
        if i + 2 < n:
            now[i+2] = not now[i+2]

print(cnt)

