a=input()
tmp=''
res=0
for item in a:
    if item==tmp:
        res+=5
    else:
        res+=10
        tmp=item
print(res)