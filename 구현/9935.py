from sys import stdin

ss = stdin.readline().rstrip()
bomb = stdin.readline().rstrip()
check = []
for s in ss:
    check.append(s)

    if len(check) >= len(bomb):
        tmp = "".join(check[-len(bomb):])
        if tmp == bomb:
            cnt = 0
            while cnt < len(bomb):
                check.pop()
                cnt += 1

if len(check) == 0:
    print("FRULA")
else:
    print("".join(check))