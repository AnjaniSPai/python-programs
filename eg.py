l=[2,3,5,1,3]
ex=3
m=max(l)
res=[]
for i in l:
    if i+ex>=m:
        res.append(True)
    else:
        res.append(False)
        return res