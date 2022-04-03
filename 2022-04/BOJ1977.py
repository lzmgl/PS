import sys
sum=0
M=int(sys.stdin.readline())
N=int(sys.stdin.readline())
p_factor=1
while 1:
    if p_factor**2<M:
        p_factor+=1
    else:
        ans2=p_factor**2
        break
while 1:
    if p_factor**2<=N:
        sum+=p_factor**2
        p_factor+=1
    else:
        break
if sum<1:
    print(-1)
    exit()
print(sum)
print(ans2)
'''
M=int(input())
N=int(input())
r=[i*i for i in range(101)if M<=i*i<=N]
print("%d\n%d"%(sum(r),r[0])if r else"-1")
'''