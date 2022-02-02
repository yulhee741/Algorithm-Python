N, K = map(int, input().split())
coin  = []
result = 0

for i in range(N) :
  coin.append(int(input()))

#단위가 큰 돈 순서대로 정렬
coin.sort(reverse=True)

# K가 0이 되면 while문 탈출
while K != 0:
  for i in coin:
    # 몫 구하기
    share = K // i
    K -= share * i
    result += share

print(result)