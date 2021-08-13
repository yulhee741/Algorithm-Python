# 괄호의 값
from sys import stdin

brackets = stdin.readline().rstrip()

def check_brackets(ss):
    stack = []
    for s in ss:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')' and stack:
            if stack[-1] == '(':
                stack = stack[:-1]
            else:
                stack.append(s)
        elif s == ']' and stack:
            if stack[-1] == '[':
                stack = stack[:-1]
            else:
                stack.append(s)
        else:
            stack.append(s)
    if stack:
        return False
    else:
        return True

def cal(ss):
    stack = []
    for s in ss:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                tmp = 0
                for i in range(len(stack) - 1, -1, -1):
                    print(i)
                    if stack[i] == '(':
                        stack[-1] = tmp * 2
                        break
                    else:
                        tmp += stack[i]
                        stack = stack[:-1]
        elif s == ']':
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                tmp = 0
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == '[':
                        stack[-1] = tmp * 3
                        break
                    else:
                        tmp += stack[i]
                        stack = stack[:-1]
    return sum(stack)

if check_brackets(brackets) == False:
    print(0)
else:
    print(cal(brackets))