# 1904번 01타일
# DP
# https://www.acmicpc.net/problem/1904
import sys, os
sys.stdin = open('{}/BOJ1904.txt'.format(os.path.dirname(os.path.realpath(__file__))))
mod=15746
N=int(sys.stdin.readline())
dp=[1]*(N+1)
dp[1]=1
try:
    dp[2]=2
    dp[3]=3
    for i in range(3, N+1):
        dp[i]=(dp[i-1]+dp[i-2])%mod
except:
    pass
print(dp[N])