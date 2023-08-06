# 1102번 발전소
# https://www.acmicpc.net/problem/1102
import sys, os

sys.stdin = open("{}/BOJ1102.txt".format(os.path.dirname(os.path.realpath(__file__))))
N = int(input().strip())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
bit = input().strip()
bit = bit[::-1]

cur, cnt = 0, 0
for m in bit:
    cur <<= 1
    if m == "Y":
        cur |= 1
        cnt += 1
p = int(input().strip())
if cnt >= p:
    print(0)
    exit()
if cnt == 0:
    print(-1)
    exit()
dp = [float("inf")] * (1 << N)


def DFS(cur, cnt):
    if cnt >= p:
        return 0

    if dp[cur] != float("inf"):
        return dp[cur]

    for i in range(N):
        if cur & (1 << i):
            for j in range(N):
                if cur & (1 << j) == 0:
                    dp[cur] = min(dp[cur], DFS(cur | 1 << j, cnt + 1) + data[i][j])

    return dp[cur]


ans = DFS(cur, cnt)
if ans != float("inf"):
    print(ans)
else:
    print(-1)
