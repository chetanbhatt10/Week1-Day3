a=int(input("Enter Your Number:"))
sum=0
for i in range(1,a):
    if(a%i==0):
        sum+=i
if(a==sum):
    print("Perfect NUMber ")
else:
    print("NOT A PERFECT NUMBER")
