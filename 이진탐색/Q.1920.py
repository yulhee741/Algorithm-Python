from sys import stdin, stdout
n = stdin.readline()
N = set(stdin.readline().split())
m = stdin.readline()
M = stdin.readline().split()

for num in M:
    stdout.write('1\n') if num in N else stdout.write('0\n')