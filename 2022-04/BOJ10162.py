import sys
T=int(sys.stdin.readline())
A=0
B=0
C=0
if T%10>0:
    print(-1)
    exit()
while T>0:
    if T>=300:
        A+=1
        T-=300
    elif T>=60:
        B+=1
        T-=60
    else:
        C+=(T//10)
        break
print(A,B,C)