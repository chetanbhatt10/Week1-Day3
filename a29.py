st=input("ENTER YOUR STRING : ")
charact=input("ENTER CHARACTER YOU WANTS TO CHECK: ")
num=0
for i in range(len(st)):
    if(charact==st[i]):
        num+=1
print(num)


