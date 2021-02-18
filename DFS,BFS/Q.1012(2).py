import sys
sys.setrecursionlimit(100000)

T = int(sys.stdin.readline())
while T != 0:
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[0 for j in range(m)] for i in range(n)]
    visited = [[0 for j in range(m)] for i in range(n)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        matrix[y][x] = 1

    def dfs(dx,dy):
        if (visited[dx][dy] == 0): 
            visited[dx][dy] += 1
            if (field[dx][dy] == 1): 
                if (dx>0): # 왼쪽
                    if (visited[dx-1][dy]==0):
                        dfs(dx-1,dy)     
                if (dy>0): # 위쪽
                    if (visited[dx][dy-1]==0):
                        dfs(dx,dy-1)
                if (dx<n-1): # 오른쪽
                    if (visited[dx+1][dy]==0):
                        dfs(dx+1,dy)     
                if (dy<n-1): # 아래쪽
                    if (visited[dx][dy+1]==0):
                        dfs(dx,dy+1)

    for i in range(n): 
        for j in range(m):
            if (visited[i][j] == 0 and field[i][j] == 1):
                dfs(i,j)
                cnt += 1
                     
 
    print(cnt)
    T -= 1