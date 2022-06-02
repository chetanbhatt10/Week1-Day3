N=input("ENTER YOUR string : ")
cnta=0
cntd=0
cnts=0
for a in range(len(N)):
    if((a>='a' and a<='z') or (a>='A' and a<='Z')):
        cnta+=1
    elif(a>'0' or a<'9'):
        cntd+=1
    else:
        cnts+=1
print("ALPHABETS ARE: ",cnta)
print("DIGITS ARE: ",cntd)
print("SPECIAL CHARACTERS ARE:",cnts)