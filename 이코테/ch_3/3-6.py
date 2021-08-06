# 1이 될 때까지
from sys import stdin

n, k = map(int, stdin.readline().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때)반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

result += n - 1
print(result)