# 2747번
# https://www.acmicpc.net/problem/2747
import sys
N=int(sys.stdin.readline())
fibo=[0,1]
for i in range(2,N+1):
    fibo.append(fibo[i-1]+fibo[i-2])
print(fibo[N])