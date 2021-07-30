# 안전 영역
import sys 
from collections import deque

def bfs(a,b,h):
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]

  queue=deque()
  queue.append((a,b))

  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=n:
        continue
      elif copy[nx][ny]==1:
        copy[nx][ny]=0
        queue.append((nx,ny))

n=int(input())
graph=[]
for i in range(n):
  graph.append(list(map(int, input().split())))

result=[]

for k in range(0,101):
  copy=[[0]*n for _ in range(n)]
  cnt=0
  for i in range(n):
    for j in range(n):
      if graph[i][j]>k:
        copy[i][j]=1

  for i in range(n):
    for j in range(n):
      if copy[i][j]==1:
        copy[i][j]=0
        bfs(i,j,k)
        cnt+=1

  result.append(cnt)

print(max(result))