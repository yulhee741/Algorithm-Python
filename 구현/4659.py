# 비밀번호 발음하기
from sys import stdin
vowels ='aeiou'

while True:
    s = stdin.readline().rstrip()
    ch1,ch2= 0,0
    if s == "end":
        break
    for i in s:
        if i in vowels:
            ch1 = 1
            break

    for i in range(1,len(s)):
        if s[i] == s[i-1] and s[i] not in 'eo':
            ch2 = 1
    
    for i in range(len(s)-2):
        if s[i] in vowels:
            if s[i+1] in vowels and s[i+2] in vowels:
                ch2 = 1
        elif s[i] not in vowels:
            if s[i+1] not in vowels and s[i+2] not in vowels: 
                ch2=1
    
    if ch1 == 0 or ch2 == 1:
        print("<" + s + "> is not acceptable." )
    elif ch1 == 1 and ch2 == 0:
        print("<" + s + "> is acceptable." )