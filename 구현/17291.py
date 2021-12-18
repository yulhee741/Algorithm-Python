from sys import stdin
n = int(stdin.readline().rstrip())

bug = [ 0 for _ in range(21) ]
bug[0], bug[1] = 1, 1

for i in range(2, n+1):
    if i % 2 == 0:
        bug[i] = bug[i-1] * 2 - bug[i-4] - bug[i-5]
    else:
        bug[i] = bug[i-1] * 2

print(bug[n])