a=input("ENTER YOUR STRING : ")
cntv=0
cntc=0
for i in range(len(a)):
    if(a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u' or a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U'):
        cntv+=1
    else:
        cntc+=1
print("NUMBER OF VOVELS ARE :",cntv)
print("NUMBER OF CONSONENTS ARE :",cntc)