# 9465번 스티커
# https://www.acmicpc.net/problem/9465
import sys, os
sys.stdin = open('{}/BOJ9465.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    data=[list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    if N==1:
        print(max(data[0], data[1]))
        exit()
    dp = [[0] *(N) for _ in range(2)]
    dp[0][0], dp[1][0] = data[0][0], data[1][0]
    for j in range(1, N):
        for i in range(2):
            dp[i][j]=max(dp[i-1][j-1], dp[i-1][j-2]) + data[i][j]
    print(max(dp[0][-1], dp[1][-1]))