import sys
n = int(sys.stdin.readline())
house = [list(map(int, list(input()))) for i in range(n)]
visited = [[0 for j in range(n)] for i in range(n)]
answer =[] # 집 수
cnt = 0 # 단지 개수

def dfs(dx,dy):
    if (visited[dx][dy] == 0): 
        visited[dx][dy] += 1
        if (house[dx][dy] == 1): 
            answer[cnt-1] +=1 
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
    for j in range(n):
        if (visited[i][j] == 0 and house[i][j] == 1):
            answer.append(0) # 단지 내 집 수
            cnt += 1 # 단지 수
        
        dfs(i,j)

print(cnt)
answer.sort()
for i in range(len(answer)):
    print(answer[i])