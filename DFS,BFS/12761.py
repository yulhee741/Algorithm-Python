# 돌다리
from sys import stdin
from collections import deque

a, b, n, m = map(int, stdin.readline().split())

graph = [0 for i in range(100001)]
visited = [0 for i in range(100001)]

dx = [-1, 1, -a, a, -b, b, a, b]

def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        x = q[0]
        del q[0]

        for i in range(8):
            if i < 6:
                nx = x + dx[i]

                if 0 <= nx < 100001 and visited[nx] == 0:
                    q.append(nx)
                    visited[nx] = 1
                    graph[nx] = graph[x] + 1

            else:
                nx = x * dx[i]
                if 0 <= nx < 100001 and visited[nx] == 0:
                    q.append(nx)
                    visited[nx] = 1
                    graph[nx] = graph[x] + 1
    return graph[m]

print(bfs(n))