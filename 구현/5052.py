# 전화번호 목록
from sys import stdin

t = int(stdin.readline().rstrip())

for _ in range(t):
    n = int(stdin.readline().rstrip())
    numbers = ["".join(list(stdin.readline().rstrip())) for _ in range(n)]
    flag = True
    numbers.sort()
    for i in range(n-1):
        if flag == True:
            numbers[i+1] = numbers[i+1].replace(numbers[i],'_')
            if "_" == numbers[i+1][0]:
                print("NO")
                flag = False
                break
        else:
            break
    else:
        print("YES")


