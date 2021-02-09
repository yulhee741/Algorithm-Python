string = list(input())
stack = []
num = 0
# 레이저 나오면 스택 길이 num에 저장, 닫는괄호나오면 +1
for i in range(len(string)):
    if string[i] == '(':
        stack.append(string[i])
    elif string[i] == ')':
        if string[i-1] =='(':
            stack.pop(-1)
            num += len(stack)
        else:
            stack.pop(-1)
            num += 1
print(num)


    

