# 교육과정설계(큐)
from sys import stdin
from collections import deque
need = stdin.readline()
n = int(stdin.readline())
for i in range(n):
    plan = stdin.readline()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))