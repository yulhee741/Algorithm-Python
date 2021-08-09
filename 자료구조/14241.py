# 슬라임 합치기
from sys import stdin

N = int(stdin.readline().rstrip())
slime = sorted(list(map(int, stdin.readline().split())), reverse=True)

score = 0
for i in range(len(slime)-1):
    size = slime[i] + slime[i+1]
    score += slime[i] * slime[i+1]
    slime[i+1] = size

print(score)

    


