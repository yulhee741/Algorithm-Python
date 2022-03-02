# 동전 분배하기
from sys import stdin

def DFS(l):
    global res
    if l == n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res = cha
    else:
        for i in range(3):
            money[i] += coin[l]
            DFS(l+1)
            money[i] -= coin[l]

if __name__=="__main__":
    n=int(stdin.readline())
    coin = []
    money = [0] * 3
    res = 2147000000
    for _ in range(n):
        coin.append(int(stdin.readline()))
    DFS(0)