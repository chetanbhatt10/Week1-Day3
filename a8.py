def pronic(a):
    for i in range(1,a+1):
        if(i*(i+1)==a):
            return 1
    return 0
for i in range(1,101):
    if(pronic(i)==1):
        print(i)