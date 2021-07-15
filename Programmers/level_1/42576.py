# 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    hash = {}
    for p in participant:
        if p in hash.keys():
            hash[p] += 1
        else:
            hash[p] = 1
            
    for c in completion:
        if c in hash.keys():
            hash[c] -= 1
    
    for i in hash.keys():
        if hash[i] != 0:
            answer = i
            
    return answer