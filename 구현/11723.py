# 집합
from sys import stdin

m = int(stdin.readline().rstrip())
s = []
for _ in range(m):
    command = stdin.readline().split()
    if len(command) > 1:
        num = int(command[1])
    if command[0] == 'add':
        if not num in s:
            s.append(num)
    elif command[0] == 'check':
        print("1") if num in s else print("0")
    elif command[0] == 'remove':
        if num in s:
            s.remove(num)
    elif command[0] == 'toggle':
        s.remove(num) if num in s else s.append(num)
    elif command[0] == 'all':
        s = list(i for i in range(1, 21))
    elif command[0] == 'empty':
        s = []
