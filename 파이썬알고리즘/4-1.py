# 가장 큰 수 (스택)
from sys import stdin

num, m = map(int, stdin.readline().split())
num = list(map(int, str(num)))
stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)