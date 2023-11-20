import sys
import bisect

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

ans = [0] * N
dp = [-1000000001]
for i in range(N):
    if data[i] > dp[-1]:
        dp.append(data[i])
        ans[i] = len(dp)
    else:
        temp = bisect.bisect_left(dp, data[i])
        dp[temp] = data[i]
        ans[i] = temp + 1

temp = [0] * len(dp)
cnt = len(dp)

for i in range(len(data) - 1, -1, -1):
    if ans[i] == cnt:
        cnt -= 1
        temp[cnt] = data[i]

print(len(dp) - 1)