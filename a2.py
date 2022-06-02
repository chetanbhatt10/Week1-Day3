a=int(input("Enter your Number:"))
temp=a
reverse=0
remainder=0
while(temp>0):
    remainder=temp%10
    temp=temp//10
    reverse=reverse*10+remainder
if(reverse==a):
    print("YES")
else:
    print("NO")