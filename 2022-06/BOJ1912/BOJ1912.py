# 1912번 연속합
# https://www.acmicpc.net/problem/1912
import sys, os
sys.stdin = open('{}/BOJ1912.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
data=list(map(int, sys.stdin.readline().split()))
dp=[0]*N
dp[0]+=data[0]
for i in range(1,N):
    dp[i]=data[i]+max(dp[i-1], dp[i])
print(max(dp))