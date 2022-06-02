def ISprime(a):
    chk=1
    for i in range(2,a):
        if(a%i==0):
            chk=0
            break
        else:
            chk=1
    if(chk==1):
        return 1
    else:
        return 0
a=int(input("ENTER YOUR NUMBER"))
for i in range(2,a+1):
    if(a%i==0):
        if(ISprime(i)==1):
            print(f"{i} is PRime Factor of number")
        


