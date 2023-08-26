# 11053번 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
import sys, os

sys.stdin = open("{}/BOJ11053.txt".format(os.path.dirname(os.path.realpath(__file__))))
N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if data[j] < data[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))
