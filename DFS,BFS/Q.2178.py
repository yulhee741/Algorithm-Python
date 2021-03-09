from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]
count_graph = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

queue = [[0, 0]]
visited[0][0] = True
count_graph[0][0] = 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while queue:
    y, x = queue.pop(0)

    if x == M and y == N:
        break

    for i in range(4):
        nX = x + dx[i]
        nY = y + dy[i]

        if 0 <= nX < M and 0 <= nY < N:
            if graph[nY][nX] == 1 and not visited[nY][nX]:
                visited[nY][nX] = True
                queue.append([nY, nX])
                count_graph[nY][nX] += count_graph[y][x] + 1

print(count_graph[N-1][M-1])