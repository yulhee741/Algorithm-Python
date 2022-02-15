# 재귀함수를 이용한 이진수 출력
from sys import stdin

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2, end=' ')

if __name__=="__main__":
    n = int(stdin.readline())
    DFS(n)