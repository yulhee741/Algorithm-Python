# 포켓몬
from collections import Counter

def solution(nums):
    N = int(len(nums)/2)
    counter = Counter(nums)  
    
    return N if len(counter) > N else len(counter)