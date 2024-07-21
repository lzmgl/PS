# 31845번 카드 교환
# https://www.acmicpc.net/problem/31845
import sys, os

sys.stdin = open("{}/BOJ31845.txt".format(os.path.dirname(os.path.realpath(__file__))))

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
card.sort()

point = 0
dp = [[0] * 2 for _ in range(M + 1)]

for i in range(1, M + 1):
    dp[i][0] = int(-1e9)
    dp[i][1] = int(-1e9)

fin = N - 1
st = 0
for i in range(1, M + 1):
    if st > fin:
        break
    point += card[fin]
    dp[i][0] = max(dp[i][0], point)
    dp[i][1] = max(dp[i - 1][1] + card[fin], dp[i - 1][0])
    st += 1
    fin -= 1

ans = int(-1e9)
for i in range(1, M + 1):
    ans = max(ans, dp[i][0])
    ans = max(ans, dp[i][1])

print(ans)
