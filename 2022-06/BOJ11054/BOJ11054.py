# 11054번 가장 긴 바이토닉 부분 수열
# https://www.acmicpc.net/problem/11054
import sys, os
sys.stdin = open('{}/BOJ11054.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
data=list(map(int, sys.stdin.readline().split()))
data2=data[::-1]
dp=[1]*N
dpp=[1]*N
for i in range(N):
    for j in range(i):
        if data[j]<data[i] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1


for i in range(N):
    for j in range(i):
        if data2[j]<data2[i] and dpp[i]<dpp[j]+1:
            dpp[i]=dpp[j]+1
maxN=0
for i in range(N):
    tmp=dp[i]+dpp[N-1-i]
    if tmp>maxN:
        maxN=tmp
        
print(maxN-1)