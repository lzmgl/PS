# 9461번 파도반 수열
# https://www.acmicpc.net/problem/9461
import sys, os
sys.stdin = open('{}/BOJ9461.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T=int(sys.stdin.readline())
dp=[1]*101
dp[3]=dp[4]=2
for i in range(5,101):
    dp[i]=dp[i-1]+dp[i-5]
for _ in range(T):
    N=int(sys.stdin.readline())
    print(dp[N-1])