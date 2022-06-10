# 14501번 퇴사
# https://www.acmicpc.net/problem/14501
import sys, os
sys.stdin = open('{}/BOJ14501.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
<<<<<<< HEAD
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp=[0]*(N+1)
for i in range(N-1, -1, -1):
    if i+data[i][0] > N:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1], data[i][1]+dp[i+data[i][0]])
print(dp[0])
=======
>>>>>>> a3bdf077a1e78c4cd7a3634671fe25a644ab6239
