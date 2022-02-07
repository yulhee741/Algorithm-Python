# 간식 파티
from sys import stdin

n = int(stdin.readline())

score = int(stdin.readline())
dp = [score]
dp2 = [score]

for _ in range(n-1):
    score = int(stdin.readline())
    tmp = []
    for i,v in enumerate(dp):
        if v < score:
            tmp.append(dp2[i])
    dp.append(score)
    if tmp:
        dp2.append(max(tmp)+score)
    else:
        dp2.append(score)

print(max(dp2))