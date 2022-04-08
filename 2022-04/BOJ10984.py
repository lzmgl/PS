import sys
T=int(sys.stdin.readline())
for _ in range(T):
    sumC=0
    sumG=0
    N=int(sys.stdin.readline())
    for _ in range(N):
        C, G = sys.stdin.readline().split()
        sumC+=int(C)
        sumG+=float(G)*int(C)
    print(sumC,round(sumG/sumC, 1))