# 피보나치 수 5
from sys import stdin
n = int(stdin.readline().rstrip())

def fibo(n):
    if n <=1:
        return n
    return fibo(n-1)+fibo(n-2)

print(fibo(n))