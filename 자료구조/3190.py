# 뱀
from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
graph = [[0] * n for _ in range(n)]

k = int(stdin.readline().rstrip())
for _ in range(k):
    x, y = map(int, stdin.readline().split())
    graph[x-1][y-1] = 1

l = int(stdin.readline().rstrip())
plans = {}
for _ in range(l):
    x, c = stdin.readline().split()
    plans[int(x)] = c

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

time = 0
i = 1 # 오른쪽 방향
snake = deque([[0, 0]]) # 뱀 위치
nx, ny = 0, 0

while 1:
    time += 1
    nx += dx[i]
    ny += dy[i]

    if time in plans.keys():
        if plans[time] == 'D':
            i = (i+1)%4
        else:
            i = (i-1)%4

    if 0 <= nx and nx < n and 0 <= ny and ny < n:
        # 몸에 부딪힌 경우
        if [nx, ny] in snake:
            break

        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            snake.append([nx, ny])
        
        elif graph[nx][ny] == 0:
            snake.append([nx, ny])
            x, y = snake.popleft()
    else:
        break

print(time)
        

    
