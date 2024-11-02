# 24464번 득수 밥 먹이기
# https://www.acmicpc.net/problem/24464
import sys, os

sys.stdin = open("{}/BOJ24464.txt".format(os.path.dirname(os.path.realpath(__file__))))
# N = int(sys.stdin.readline())
# mod = 1000000007
# dp = [1, 1, 1, 1, 1]
# for _ in range(N - 1):
#     tp = [0, 0, 0, 0, 0]
#     tp[0] = (dp[2] + dp[3] + dp[4]) % mod
#     tp[1] = (dp[3] + dp[4]) % mod
#     tp[2] = (dp[0] + dp[4]) % mod
#     tp[3] = (dp[0] + dp[1] + dp[4]) % mod
#     tp[4] = (dp[0] + dp[1] + dp[2] + dp[3]) % mod
#     dp = tp[:]
# print(sum(dp) % mod)


N = int(sys.stdin.readline())
mod = 1000000007
dp = [[0 for _ in range(N)] for _ in range(5)]

for j in range(N):
    if j == 0:
        for i in range(5):
            dp[i][j] = 1
    else:
        for i in range(1, 5):
            dp[0][j] = (dp[0][j] + dp[i][j - 1]) % mod
            for k in range(5):
                if k != 0 and abs(k - i) <= 1:
                    continue
                dp[i][j] = (dp[i][j] + dp[k][j - 1]) % mod
res = 0
for item in dp:
    res += item[-1]
print(res % mod)
