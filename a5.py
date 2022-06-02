a=int(input("Enter Your NUmber:"))
chk=0
for i in range(2,a):
    if(a%i==0):
        chk=1
        break
    else:
        chk=0
if(chk==1):
    print("NOT A PRIME NUMBER")
else:
    print("PRIME NUMBER")
        