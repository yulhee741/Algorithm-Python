# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    sum = 0
    answer = []
    for i in range(n):
        sum += x
        answer.append(sum)
    return answer