# 하샤드 수

def solution(x):
    answer = True
    findD = []
    
    for _ in str(x):
        findD.append(int(_))
    
    if x % sum(findD) == 0:
        answer = True
    else:
        answer = False
    
    return answer