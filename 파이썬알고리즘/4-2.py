# 쇠막대기
from sys import stdin
s = stdin.readline()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s)
    else:
        stack.pop()
        if s[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)