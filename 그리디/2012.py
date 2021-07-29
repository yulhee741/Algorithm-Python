# 등수 매기기
from sys import stdin

N = int(stdin.readline())
score = []
for _ in range(N):
    score.append(int(stdin.readline()))

score.sort() # 정렬
result = 0
for i in range(N):
    if score[i] != i+1: # 리스트에 해당 번째 인덱스가 등수와 다를경우 
        result += abs(score[i]-(i+1)) # 차이를 구하여 결과에 저장

print(result)

