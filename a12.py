def fact(N):
    if(N==1):
        return 1
    else:
        return N*fact(N-1)
a=int(input("Enter your number"))
temp=a
x=0
factsum=0
while(temp>0):
    x=temp%10
    factsum+=fact(x)
    temp=temp//10
if(factsum==a):
    print("STRONG NUMBER")
else:
    print("NOT A STRONG NUMBER")

