# 창고 다각형
from sys import stdin

n = int(stdin.readline())

columns = []
for i in range(n):
    columns.append(tuple(map(int, stdin.readline().split())))

columns = sorted(columns)
max_column = max(columns, key= lambda x:x[1])
max_idx, max_height = max_column[0], max_column[1]

container = [0 for i in range(columns[-1][0]+1)]
for l,h in columns:
    container[l] = h

total = 0
tmp = 0
# 왼쪽에서부터
for i in range(max_idx+1):
    if container[i] >= tmp:
        tmp = container[i]
    total += tmp

tmp = 0
# 오른쪽에서부터
for i in range(len(container)-1, max_idx, -1):
    if container[i] >= tmp:
        tmp = container[i]
    total += tmp

print(total)


