# 1107번 리모컨
# https://www.acmicpc.net/problem/1107
import sys, os
sys.stdin = open('{}/BOJ1107.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
err=set(list(map(int,sys.stdin.readline().split())))
dep=[]
if M>9:
    print(abs(N-100))
    exit()
for i in range(999999):
    errout=True
    for item in err:
        if str(item) in str(i):
            errout=False
    if errout:
        dep.append(i)
ans=False
anslist=[]
for idx,item in enumerate(dep):
    if N <= item:
        try:
            anslist.append(dep[idx-1])
            anslist.append(dep[idx])
        except:
            anslist.append(dep[idx])
        break
minN=5000000
ans=0
if len(anslist) == 0:
    anslist.append(dep[-1])
minN=min(abs(N-anslist[0]), minN)
for item in anslist:
    if minN != min(abs(N-item), minN):
        minN=min(abs(N-item), minN)
        ans+=len(str(item))
if ans==0:
    ans+=len(str(anslist[0]))
ans+=(min(minN,abs(N-100)))

# min(근사값 -> ++ -- , 그냥++--)
ans=min(ans, abs(N-100))
print(ans)