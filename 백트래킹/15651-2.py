# N과 M(3)
import sys
input=sys.stdin.readline

def go(index, n, m):
    if index == m:
        print(' '.join(map(str, arr)))
        return 

    for i in range(n):
        arr.append(i+1)
        go(index+1, n, m)
        arr.pop()

n, m = map(int, input().split())
arr=[]

go(0, n, m)