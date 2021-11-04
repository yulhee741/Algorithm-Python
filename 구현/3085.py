# 사탕 게임
from sys import stdin
import copy

n = int(stdin.readline().rstrip())
candy = [list(stdin.readline().rstrip()) for i in range(n)]

def cnt_color(candy):
    cnt = 0
    for i in range(n):
        r_cnt = 1
        c_cnt = 1
        for j in range(n-1):
            if candy[i][j] == candy[i][j+1]:
                r_cnt += 1
            else:
                cnt = max(r_cnt, cnt)
                r_cnt = 1
            if candy[j][i] == candy[j+1][i]:
                c_cnt += 1
            else:
                cnt = max(c_cnt, cnt)
                c_cnt = 1
        cnt = max(cnt, r_cnt, c_cnt)

    return cnt


result = 0
for i in range(n):
    for j in range(n-1):
        if candy[i][j] != candy[i][j+1]:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            result = max(result, cnt_color(candy))
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

        if candy[j][i] != candy[j+1][i]:
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
            result = max(result, cnt_color(candy))
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]

print(result)
