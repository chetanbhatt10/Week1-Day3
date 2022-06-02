a=input("ENTER YOUR CHARCTER")
if((a>='a' and a<='z') or (a>='A' and a<='Z')):
    print("IT IS A ALPHABET")
elif(a>'0' or a<'9'):
    print("IT IS A DIGIT")
else:
    print("SPECIAL CHRACTERS")