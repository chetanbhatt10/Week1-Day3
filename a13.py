def fact(N):
    if(N==1):
        return 1
    else:
        return N*fact(N-1)
def strong(a):
    temp=a
    x=0
    factsum=0
    while(temp>0):
        x=temp%10
        factsum+=fact(x)
        temp=temp//10
    if(factsum==a):
        return 1
    else:
        return 0
for i in range(1,101):
    if(strong(i)==1):
        print(i)
