def palindrom(a):
    temp=a
    reverse=0
    remainder=0
    while(temp>0):
        remainder=temp%10
        temp=temp//10
        reverse=reverse*10+remainder
    if(reverse==a):
        return 1
    else:
        return 0
for i in range(1,101):
    if(palindrom(i)==1):
        print(i)
    
    