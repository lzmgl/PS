# 11659번 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659
import sys, os
sys.stdin = open('{}/BOJ11659.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, M=map(int,sys.stdin.readline().split())
data=list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N+2)]
for idx, datum in enumerate(data):
    dp[idx]=dp[idx-1] + datum
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print((dp[b-1]-dp[a-2]))