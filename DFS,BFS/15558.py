# 점프 게임

from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().rstrip())) for _ in range(2)]
visited = [[False] * n for _ in range(2)]
left, right = 0, 1

def bfs(start):
    q = deque([start])
    idx = 0

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for nx, ny in ((x, y + 1), (x, y - 1), (~x, y + k)):
                if ny >= n:
                    return 1
                if idx < ny < n and graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True

        idx += 1
    return 0

print(bfs([0,0]))