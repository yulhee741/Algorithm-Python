from sys import stdin, stdout
import bisect
n = stdin.readline()
N = list(map(int, stdin.readline().split()))
N.sort()
m = stdin.readline()
M = list(map(int, stdin.readline().split()))

for num in M:
    i = bisect.bisect(N,num)
    if N[i-1] == num:
        stdout.write('1\n')
    else:
        stdout.write('0\n')