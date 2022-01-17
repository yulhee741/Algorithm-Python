# 과제
from sys import stdin

n = int(stdin.readline().rstrip())
work = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]

work.sort()

cnt = work[-1][0]
result = 0
check = []

while True:
    if cnt == 0:
        break
    while work and work[-1][0] >= cnt:
        check.append(work.pop()[1])
    cnt -= 1

    if not check:
        continue
    check.sort()
    result += check.pop()

print(result)

