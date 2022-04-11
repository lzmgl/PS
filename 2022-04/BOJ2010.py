N=int(input())
tmp=0
for _ in range(N):
    s=int(input())
    tmp+=s
tmp-=(N-1)
print(tmp)