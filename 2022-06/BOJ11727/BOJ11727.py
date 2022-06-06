# 11727번 2×n 타일링 2
# https://www.acmicpc.net/problem/11727
import sys, os
sys.stdin = open('{}/BOJ11727.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from math import factorial
N=int(sys.stdin.readline())
mod=10007
pos=N//2
DP=[0]*(N+1)
DP[0]=1
for i in range(pos+1):
    col=N-(2*i)
    tmp=0
    for rec in range((col//2)+1):
        cur=col-(2*rec)
        tmp+=factorial(i+cur+rec)//(factorial(i)*factorial(cur)*factorial(rec))%mod
    DP[i]=((DP[i-1]+tmp)%mod)

print(DP[N//2]) #DP[i] = 가로가 i개인 경우의수.