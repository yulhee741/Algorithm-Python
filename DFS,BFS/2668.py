# 숫자 고르기
from sys import stdin
from collections import defaultdict

n = int(stdin.readline().rstrip())
node = defaultdict(list)

for i in range(1, n+1):
    num = int(stdin.readline().rstrip())
    node[num].append(i)

checked = [0 for _ in range(n+1)]
result = []

def dfs(num, visited):
    visited.add(num)
    checked[num] = 1
    for n in node[num]:
        if n not in visited:
            dfs(n, visited.copy())
        else:
            result.extend(list(visited))
            return

for i in range(1, n+1):
    if not checked[i]:
        dfs(i, set([]))

result.sort()
print(len(result))
for x in result:
    print(x)