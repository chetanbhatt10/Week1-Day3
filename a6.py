

def ISprime(a):
    chk=0
    for i in range(2,a):
        if(a%i==0):
            chk=1
            break
        else:
            chk=0
    if(chk==1):
        return 1
    else:
        return 0

for i in range(1,100):
    if(ISprime(i)==1):
        print(f"{i} is not Prime number") 
    else:
        print(f"{i} is a prime number")   