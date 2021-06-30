# 파도반 수열
import sys

T = int(sys.stdin.readline().rstrip())

def pado(N):
    pado = [1] * N 

    for i in range(3, N):
        pado[i] = pado[i-3] + pado[i-2]

    return pado[-1]


for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    result = pado(N)
    print(result)
