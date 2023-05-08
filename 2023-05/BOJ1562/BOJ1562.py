# 1562번 계단 수
# https://www.acmicpc.net/problem/1562
import sys, os
sys.stdin = open('{}/BOJ1562.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
ALL=(1<<10)-1
mod=int(1e9)
cnt=0
dp=[[[0]*(ALL+1) for _ in range(10)] for _ in range(-~N)]
for i in range(1, 10):
    dp[1][i][1<<i]=1

for i in range(2, -~N):
    for j in range(10):
        for k in range(ALL+1):
            if not j:
                dp[i][j][k|(1<<j)]+=dp[i-1][1][k]
                dp[i][j][k|(1<<j)]%=mod
            elif not j-9:
                dp[i][j][k|(1<<j)]+=dp[i-1][8][k]
                dp[i][j][k|(1<<j)]%=mod
            else:
                dp[i][j][k|(1<<j)]+=dp[i-1][j-1][k]+dp[i-1][j+1][k]
                dp[i][j][k|(1<<j)]%=mod
for i in range(10):
    cnt+=dp[-1][i][ALL]
    cnt%=ALL
print(cnt)