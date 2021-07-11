# N개의 최소공배수

def solution(arr):
    lmc = max(arr)
    while 1:
        cnt = 0
        for i in arr:
            if lmc % i == 0:
                cnt += 1
            else:
                break
        
        if cnt == len(arr):
            break
        lmc += 1
    
    return lmc