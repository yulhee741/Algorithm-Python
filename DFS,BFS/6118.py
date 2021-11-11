# 숨바꼭질
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(point):
    q = deque()
    q.append(point)
    visited[point] = 1
    
    while q:
        point = q.popleft()
        for i in graph[point]:
            if visited[i] == 0:
                visited[i] = visited[point] + 1
                q.append(i)

bfs(1)
result = max(visited)

print(visited.index(result), result - 1, visited.count(result))