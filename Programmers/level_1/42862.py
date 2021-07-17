# 체육복

def solution(n, lost, reserve):
    uniform = [1 for i in range(n)]
    
    for i in range(n):
        if i+1 in lost:
            uniform[i] -= 1
        if i+1 in reserve:
            uniform[i] += 1  
    
    for i in range(n):
        if i-1 > 0 and uniform[i] == 0:
            if uniform[i-1] == 2:
                uniform[i-1] -= 1
                uniform[i] += 1

            elif i+1 < len(uniform) and uniform[i+1] == 2:
                uniform[i+1] -= 1
                uniform[i] += 1
    
    answer = len(uniform) - uniform.count(0)
    return answer

# 다른 사람 풀이

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)