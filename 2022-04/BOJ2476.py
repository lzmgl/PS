# 2476번 주사위 게임
# https://www.acmicpc.net/problem/2476
import sys
N=int(sys.stdin.readline())
ans =0
for i in range(N):
    A,B,C = map(int,sys.stdin.readline().split())
    if A==B==C:
        res = (10000+A*1000)
    elif A!=B and A!=C and B!=C:
        res = (max(A,B,C)*100)
    else :
        if A==B:
            res = (1000+A*100)
        elif A==C:
            res = (1000+A*100)
        else:
            res = (1000+B*100)
    ans = max(ans, res)
print(ans)