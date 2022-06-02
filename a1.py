a=int(input("Enter your Number :"))
temp=a*a
x=0
while(temp>0):
    x+=temp%10
    temp=temp//10

if(x==a):
    print("NEON NUMBER")
else:
    print("NOT A NEON NUMBER")



    




