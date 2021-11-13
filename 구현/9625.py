# BABBA
from sys import stdin

k = int(stdin.readline())
a = 0
b = 1

for i in range(1, k):
    a, b = b, a + b

print(a, b)

