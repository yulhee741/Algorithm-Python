# 2+1 세일
from sys import stdin

N = int(stdin.readline().rstrip())
price = []

for _ in range(N):
    price.append(int(stdin.readline().rstrip()))

result = []
tmp = []

# 가격이 큰 순서대로 정렬
price.sort(reverse=True)

# 인덱스가 3번째인 경우 제외하고 append
for i in range(len(price)):    
    if i % 3 == 2:
        result.append(tmp)
        tmp = []
        continue

    tmp.append(price[i])

    if N % 3 == 1 and i == N-1:
        result.append([price[i]])
    if N % 3 == 2:
        if i == N-1:
            result.append([price[i]])
        elif i == N-2:
            result.append([price[i]])

sum_money = 0
for i in result:
    for j in i:
        sum_money += j

print(sum_money)
        