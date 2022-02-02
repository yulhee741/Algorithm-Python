from collections import deque

N = int(input())

for i in range(N):
    func = input()
    n = int(input())
    s = input()
    if n == 0:
        s = []
    else:
        s = deque(''.join(s[1:-1]).split(","))
    count = 0
    for i in func:
        if i == 'R':
            count += 1
        elif i == 'D':
            if len(s) == 0:
                print("error")
                break
            if count % 2 == 0:
                s.popleft()
            else:
                s.pop()


    else:
        if count % 2 == 0:
            print("[", end = "")
            print(",".join(s), end = "")
            print("]")
        else:
            s.reverse()
            print("[", end = "")
            print(",".join(s), end = "")
            print("]")