# 겉넓이 구하기
from sys import stdin

n, m = map(int, stdin.readline().split())
block= [list(map(int, stdin.readline().split())) for _ in range(n)]
block.insert(0, [0] * (m+2))
block.append([0] * (m+2))
for i in range(1, n+1):
    block[i].insert(0, 0)
    block[i].append(0)

cnt = n * m * 2
for i in range(n+1):
    for j in range(m+1):
        cnt += abs(block[i][j] - block[i+1][j])
        cnt += abs(block[i][j] - block[i][j+1])
print(cnt)