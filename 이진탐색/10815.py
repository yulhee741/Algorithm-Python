from sys import stdin

n = int(stdin.readline())
n_list = list(map(int, stdin.readline().split()))

m = int(stdin.readline())
m_list = list(map(int, stdin.readline().split()))

n_list.sort()
left = 0 
right = len(n_list)-1

def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left+right)//2
        if n_list[mid] == target:
            return 1
        elif n_list[mid]>target:
            right = mid-1
        else :
            left = mid+1
    return 0

for target in m_list:
    print(binary_search(n_list, target, left, right), end=' ')
    