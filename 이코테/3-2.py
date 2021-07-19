# 큰 수의 법칙
from sys import stdin
n, m, k = map(int, stdin.readline().split())
# 숫자 갯수, 더해야하는 횟수, k번까지만 더할 수 있음
nums = list(map(int, stdin.readline().split()))

nums.sort(reverse=True)
first = nums[0]
second = nums[1]

#가장 큰 수 더해지는 횟수
cnt = int(m / (k+1)) * k
cnt += m % (k+1)

result = 0
result += cnt * first
result += (m-cnt) * second

print(result)