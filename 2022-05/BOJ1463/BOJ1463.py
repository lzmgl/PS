# 1463번 1로 만들기
# https://www.acmicpc.net/problem/1463
import sys, os
sys.stdin = open('{}/BOJ1463.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
dp=[0]*1000001

for i in range(2, N+1):
    dp[i] = dp[i-1]+1
    if i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[N])