#신규 아이디 추천

def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    
    # 2
    for s in new_id :
        if s.isalpha() or s.isdigit() or s in ('-','_','.'):
            answer += s
    
    # 3
    while '..' in answer:
        answer = answer.replace('..','.')
            
    # 4
    if answer[0] == '.':
        if len(answer) > 1:
            answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
        
    # 5
    if len(answer) == 0:
        answer = 'a'
        
    # 6
    if len(answer) >= 16:
        answer = answer[:15]   
    if answer[-1] == '.':
        answer = answer[:-1]
        
    # 7
    if len(answer) <= 2:
        while len(answer) <= 2:
            answer += answer[-1]
    
    return answer