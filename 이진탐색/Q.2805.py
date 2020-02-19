from sys import stdin
N, M = map(int,stdin.readline().split())
arr = sorted(list(map(int, stdin.readline().split())))

def solve():
    low, high = 1, max(arr)
    ans = 0
    while low <= high:
        middle = (low + high) // 2
        length = 0
        for n in arr:
            if n > middle:
                length += n - middle
        if length >= M:
            low = middle + 1
            ans = middle
        else:
            high = middle - 1
    return ans
    
print(solve())