# 지구 온난화
from sys import stdin
import copy

r, c = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for i in range(r)]
plan = copy.deepcopy(board)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


for y in range(r):
    for x in range(c):
        if board[y][x] == 'X':
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if ny == r or ny == -1 or nx == c or nx == -1:
                    cnt += 1
                    continue
                if 0 <= nx < c and 0 <= ny < r:
                    if board[ny][nx] == '.':
                        cnt += 1

            if cnt >= 3:
                plan[y][x] = '.'
                cnt = 0


# 바다 제거
def rotated(a):
    n = len(a)
    m = len(a[0])
    
    result = [[0]* n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
            
    return result


#1번째 C_start 2번째 R_end 3번째 C_end 4번째 R_start
point = [0,0,0,0]
tmp = copy.deepcopy(plan)
for r in range(4):
    tmp = rotated(tmp)
    for i in tmp:
        if not 'X' in i:
            point[r] += 1
        else:
            break

C_start, R_end, C_end, R_start = point[0], point[1], point[2], point[3]
for i in range(R_start, len(plan)-R_end):
    for j in range(C_start, len(plan[0])-C_end):
        print(plan[i][j], end='')
    print()



