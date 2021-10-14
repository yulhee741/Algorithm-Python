# N과 M(4)
import sys
input=sys.stdin.readline

def go(index, ck, n, m):
    if index == m:
        print(' '.join(map(str, arr)))
        return 

    for i in range(ck, n):
        arr.append(i+1)
        go(index+1, i , n, m)
        arr.pop()

n, m = map(int, input().split())
arr=[]

go(0, 0, n, m)