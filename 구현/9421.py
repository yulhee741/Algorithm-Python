# 소수상근수
from sys import stdin

def square(n):
    sum_n = 0
    while n != 0:
        digit = n % 10
        n //= 10
        sum_n += digit * digit
    return sum_n

N = int(stdin.readline())
ch = [0]*(N+1)
nums = []
result = []
for i in range(2, N+1):
    if ch[i] == 0:
        nums.append(i)
        for j in range(i, N+1, i):
            ch[j] = 1

for num in nums:
    tmp = []
    check = num
    tmp.append(num)
    idx = 0
    while tmp:
        n = tmp[idx]
        res = square(n)
        if res == 1:
            result.append(check)
            break
        elif res in tmp:
            break
        else:
            tmp.append(res)
        idx += 1

for res in result:
    print(res)
