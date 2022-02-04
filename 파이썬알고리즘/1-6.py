# 자릿수의 합
from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

# def digit_sum(x):
#     sum = 0
#     while x > 0:
#         sum += x%10
#         x = x//10

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum
    
max = -2147000000

for x in a:
    total = digit_sum(x)
    if total > max:
        max = total
        res = x

print(res)

