# 문자열 압축
def solution(s):
    answer = len(s)
    
    for i in range(1, (len(s)//2)+1):
        copy_s = s
        cnt = 1
        prev = ''
        result = ''
        
        while len(copy_s) >= i:
            now = copy_s[:i]
            copy_s = copy_s[i:]
            
            if prev == now:
                cnt += 1
            else:
                if cnt != 1: 
                    result += str(cnt)
                result += prev # 이전 문자열 result에 저장
                prev = now
                cnt = 1
                
        # 마지막 문자열 처리
        if cnt != 1:
            result += str(cnt)
        result += prev
        result += copy_s
        
        if answer > len(result):
            answer = len(result)
            
    return answer