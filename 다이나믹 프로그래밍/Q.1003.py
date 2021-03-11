from sys import stdin
T = int(stdin.readline())

for i in range(T):
    num = int(stdin.readline())
    zero = 1
    one = 0
    tmp = 0
    for j in range(num):
        tmp = one
        one = one + zero
        zero = tmp
    print(zero, one)


