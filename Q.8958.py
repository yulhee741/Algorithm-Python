N = int(input())

for i in range(N) :
    O_num = 0
    Total = 0
    OX = input()
    for s in OX:
        if s == 'O':
            O_num += 1
        elif s == 'X':
            O_num = 0
        Total += O_num
    print(Total)

