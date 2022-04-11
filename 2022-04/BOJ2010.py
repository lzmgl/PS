import sys
N=int(sys.stdin.readline())
tmp=0
for _ in range(N):
    s=int(sys.stdin.readline())
    tmp+=s
tmp-=(N-1)
print(tmp)