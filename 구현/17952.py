# 과제는 끝나지 않아!
from sys import stdin

n = int(stdin.readline().rstrip())
result = 0
check_list = []

def check_time(time, score):
    if time == 0:
        global result
        result += score
    else:
        check_list.append((time, score))
    return


for _ in range(n):
    work = list(map(int, stdin.readline().split()))
    
    if work[0] == 1:
        time, score = work[2] - 1, work[1]
        check_time(time, score)

    elif work[0] == 0:
        if check_list:
            time, score = check_list.pop()
            time -= 1
            check_time(time, score)
        
print(result)