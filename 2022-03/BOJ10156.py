import sys
K,N,M = map(int,sys.stdin.readline().split())
res=K*N-M
if res > 0:
    print(res)
else:
    print("0")