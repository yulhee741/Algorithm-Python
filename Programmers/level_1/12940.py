# 최대공약수와 최소공배수

def gcd(x, y):
    if x < y:
        x, y = y, x
    while y:
        x, y = y, x % y
    return x


def lmc(x, y):
    return x * y // gcd(x,y)
    
    
def solution(n, m):
    answer = []
    answer.append(gcd(n, m))
    answer.append(lmc(n, m))
    return answer