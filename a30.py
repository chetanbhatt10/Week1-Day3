a=input("STRING IS: " )
chardict={}
for i in a:
    keys=chardict.keys()
    if i in keys:
        chardict[i]+=1
    else:
        chardict[i]=1
print(chardict)