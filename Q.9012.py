N = int(input())
# 스택을 사용해서 -> 여는 괄호면 push 닫는 괄호면 pop
# 괄호 문자열을 한바퀴 다 돌았을 때 길이가 0이면 성공
# 닫는 괄호를 더 많이 뺄 때를 고려하여 닫는 괄호일 때 스택 리스트 길이 한번 더 확인
for i in range(N):
    stack = []
    vps = input()
    flag = 0
    for s in vps:
        if s == '(':
            stack.append(s)
        else :
            if len(stack) == 0:
                print('NO')
                flag = 1
                break
            else:
                stack.pop(-1)
    if flag == 0:
        if len(stack) != 0:
            print('NO')
        elif len(stack) == 0:
            print('YES')