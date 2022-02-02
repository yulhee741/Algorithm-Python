case=0
while 1:
    case += 1 
    l,p,v=map(int,input().split())
    if l==0 and p==0 and v==0:
        break
    count = 0
    n = v // p
    count += n * l
    if v - (n * p) <= l:
        count += v - (n * p)
    #교훈: 반례를 조심하자..
    else:
        count += l
    
    print("Case "+str(case)+": " +str(count) )