import sys

N=int(sys.stdin.readline())
for _ in range(N):
    p=int(sys.stdin.readline())
    maxC=0
    for _ in range(p):
        C, name = sys.stdin.readline().split()
        C=int(C)
        tmp = max(maxC, C)
        if maxC != tmp:
            maxC=tmp
            ans = name
    print(ans)