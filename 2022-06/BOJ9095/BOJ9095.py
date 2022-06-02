# 9095번 1, 2, 3 더하기
# DP, 다이나믹 프로그래밍
# https://www.acmicpc.net/problem/9095
import sys, os
sys.stdin = open('{}/BOJ9095.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T=int(sys.stdin.readline())
DP=[0, 1, 2, 4]
for i in range(4,12):
    DP.append(DP[i-1]+DP[i-2]+DP[i-3])
for _ in range(T):
    n=int(sys.stdin.readline())
    print(DP[n])