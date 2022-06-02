a=int(input("ENTER THE NUMBER"))
sum=0
while(a>0):
    x=a%10
    sum+=x
    a=a//10
print("THE SUM OF DIGITS ARE ",sum)
