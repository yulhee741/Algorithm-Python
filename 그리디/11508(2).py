# 2+1 세일
from sys import stdin

N = int(stdin.readline().rstrip())
price = []

for _ in range(N):
    price.append(int(stdin.readline().rstrip()))

result = 0

price.sort(reverse=True)
# 큰 순서대로 정렬 후, 인덱스가 세번째가 아닌 요소 값만 result에 더하기
for i in range(len(price)):    
    if i % 3 != 2:
        result += price[i]

print(result)
        