# 한 줄로 서기
from sys import stdin

N = int(stdin.readline().rstrip()) # 사람 수
line = list(map(int, stdin.readline().split()))
result = []


for i in range(N-1, -1, -1):
    result.insert(line[i], i+1)


print(*result)
    