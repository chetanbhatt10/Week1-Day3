a=int(input("Enter Your Number"))
temp=a
rev=0
rem=0

while(temp>0):
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
print(f"REVERSE OF NUMBER {a} is{rev}")
    