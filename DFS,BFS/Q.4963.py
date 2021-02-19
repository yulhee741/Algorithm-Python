from sys import stdin

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
def bfs(i, j):
    mat[i][j] = 0
    queue = [[i, j]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(8):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < h and 0 <= y < w and mat[x][y] == 1:
                mat[x][y] = 0
                queue.append([x, y])

while True:
    w, h = map(int, stdin.readline().split())
    if w == 0 and h == 0:
        break
    mat = []
    cnt = 0
    for i in range(h):
        mat.append(list(map(int, stdin.readline().split())))
    for i in range(h):
        for j in range(w):
            if mat[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)