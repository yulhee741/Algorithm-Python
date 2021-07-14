# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    bucket = []
    
    for m in moves:
        if len(bucket) > 1 and bucket[-1] == bucket[-2]:
            del bucket[-2]
            del bucket[-1]
            answer += 2
            
        for n in board:
            if n[m-1] != 0:
                bucket.append(n[m-1])
                n[m-1] = 0
                break
                
    return answer