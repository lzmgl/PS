# 2568번 전깃줄 - 2
# https://www.acmicpc.net/problem/2568
import sys, os

sys.stdin = open("{}/BOJ2568.txt".format(os.path.dirname(os.path.realpath(__file__))))

import bisect

tmp = []
N = int(sys.stdin.readline())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    tmp.append((a, b))
tmp.sort()
data = [0]
for item in tmp:
    data.append(item[1])

tmp = []
ans = [0] * (N + 1)
dp = [-1000000001]
for i in range(1, N + 1):
    if data[i] > dp[-1]:
        dp.append(data[i])
        ans[i] = len(dp)
    else:
        temp = bisect.bisect_left(dp, data[i])
        dp[temp] = data[i]
        ans[i] = temp + 1
        tmp.append(i)

temp = [0] * len(dp)
cnt = len(dp)

for i in range(len(data) - 1, -1, -1):
    if ans[i] == cnt:
        cnt -= 1
        temp[cnt] = data[i]
print(dp)
print(len(tmp))
for c in tmp:
    print(c)
