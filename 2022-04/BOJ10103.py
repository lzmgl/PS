import sys
N=int(sys.stdin.readline())
S=C=100
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a<b:
        S-=b
    elif a>b:
        C-=a
print(S, C)