a=int(input("Enter Your Number:"))
sum=0
x=0
prod=1
while(a>0):
    x=a%10
    a=a//10
    sum+=x
    prod*=x
    
print("THE SUM OF DIGITS IS:",sum)
print("THE PRODUCT OF DIGITS IS:",prod)
if(sum==prod):
    print("YES IT IS A SPY NUMBER")
else:
    print("NOT A SPY NUMBER")


    