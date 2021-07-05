# 나이트의 이동
from sys import stdin
from collections import deque


T = int(stdin.readline())

for _ in range(T):
    # 체스판 한 변의 길이
    I = int(stdin.readline())
    # 나이트가 현재 있는 칸
    now_x, now_y = map(int, stdin.readline().split())
    # 나이트가 이동하려고 하는 칸
    dis_x, dis_y = map(int, stdin.readline().split())
    # 그래프 생성
    visited = [[0] * I for i in range(I)]
    visited[now_x][now_y] = 1

    dx = [1, -1, 2, 2, -2, -2, 1, -1]
    dy = [2, 2, 1, -1, 1, -1, -2, -2]

    dQ = deque()
    dQ.append((now_x, now_y, 0))

    while dQ:
        now = dQ.popleft()
        x, y = now[0], now[1]

        if x == dis_x and y == dis_y:
            print(now[2])
            break

        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < I and 0 <= ny < I:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    dQ.append((nx, ny, now[2]+1))