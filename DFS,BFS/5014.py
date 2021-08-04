# 스타트 링크
from sys import stdin
from collections import deque
# 총 F층, 강호가 있는 곳 S층, 스타트링크 위치 G층
F, S, G, U, D = map(int, stdin.readline().split())
visited = [0 for _ in range(F+1)]

def bfs():
    q = deque()
    q.append((S, 0))
    visited[S] = 1

    while q:
        now, result = q.popleft()
        if now == G:
            return result
        if now + U <= F and visited[now + U] == 0:
            q.append((now + U, result + 1))
            visited[now + U] = 1
        if now - D >= 1 and visited[now - D] == 0:
            q.append((now - D, result + 1))
            visited[now - D] = 1

result = bfs()
if result == None:
    print("use the stairs")
else:
    print(result)