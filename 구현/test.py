N = input("숫자입력")
rev_N = 0
for i in range(1, len(N)+1):
    rev_N += int(N[-i]) * (10**(len(N)-i))
print(rev_N)
