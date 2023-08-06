# 1562번 계단 수
# https://www.acmicpc.net/problem/1562
import sys, os

sys.stdin = open("{}/BOJ1562.txt".format(os.path.dirname(os.path.realpath(__file__))))
N = int(sys.stdin.readline())
ALL = (1 << 10) - 1
mod = int(1e9)
cnt = 0
dp = [[[0] * (ALL + 1) for _ in range(10)] for _ in range(N + 1)]
# dp[i][j][k] i=N+1 j=10 k=1024
for i in range(1, 10):  # 각 자리수마다 1로 initialize
    dp[1][i][1 << i] = 1

for i in range(2, N + 1):
    for j in range(10):
        for k in range(ALL + 1):
            if not j:  # 0옆엔 1만 가능
                dp[i][j][k | (1 << j)] += dp[i - 1][1][k]
                dp[i][j][k | (1 << j)] %= mod
            elif not j - 9:  # 9옆엔 8만 가능
                dp[i][j][k | (1 << j)] += dp[i - 1][8][k]
                dp[i][j][k | (1 << j)] %= mod
            else:  # 그 외엔 -1 +1 모두 가능
                dp[i][j][k | (1 << j)] += dp[i - 1][j - 1][k] + dp[i - 1][j + 1][k]
                dp[i][j][k | (1 << j)] %= mod
            # 각 k | (1 << j) 에 경우의 수를 더해 최종적으로 111111111 (0~9 모두 사용)한 경우를 더해줌.
for i in range(10):
    cnt += dp[-1][i][ALL]
    cnt %= mod
print(cnt)
