# 괄호 변환
        
def right(u, v):
    ss = '(' + v + ')'
    u = u[1:-1]
    for s in u:
        if s == '(':
            ss += ')'
        else:
            ss += '('
    print(ss)
    return ss

def set_uv(w):
    l, r = 0, 0
    if w == "":
        return ""

    for i in range(len(w)):
        if w[i] == '(':
            l += 1
        elif w[i] == ')':
            r += 1
        if l == r:
            if w[i] == ')':
                return w[:i+1] + set_uv(w[i+1:])
            else:
                return right(w[:i+1], set_uv(w[i+1:]))
    

def solution(p):
    return set_uv(p)
