import itertools

N, S = map(int, input().split())
nums=[int(i) for i in input().split()]
result = 0

for i in range(1, len(nums)+1):
    nCr = list(itertools.combinations(nums,i))
    for j in nCr:
        if sum(j) == S:
            result += 1

print(result)
        
