N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):

    visited[0][0] = 1
    queue = [(0,0)]

    while queue:
        now = queue.pop(0)
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if visited[nx][ny] == 0 and maze[nx][ny] == '1':
                    visited[nx][ny] == visited[now[0]][now[1]] + 1
                    queue.append((nx,ny))
                    
    return visited[-1][-1]

print(bfs(0,0))