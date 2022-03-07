# 사과나무(BFS)
from sys import stdin
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(stdin.readline())
a = [list(map(int, stdin.readline().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
apple = 0
q = deque()
ch[n//2][n//2] = 1
apple += a[n//2][n//2]
q.append((n//2, n//2))
l = 0
while True:
    if l == n//2:
        break
    size = len(q)
    for i in range(size):
        tmp = q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                apple += a[x][y]
                ch[x][y] = 1
                q.append((x,y))
    l += 1