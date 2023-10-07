# 2568번 전깃줄 - 2
# https://www.acmicpc.net/problem/2568
import sys, os

sys.stdin = open("{}/BOJ2568.txt".format(os.path.dirname(os.path.realpath(__file__))))

import bisect

N = int(sys.stdin.readline())
data = {}
arr = []
dp = [-1]
ans = []
backtrace = []

for i in range(N):
    a, b = map(int, input().split(" "))
    data[b] = a
temp = sorted(data)
for i in temp:
    arr.append(data.get(i))
for i in arr:
    if i > dp[-1]:
        dp.append(i)
    else:
        dp[bisect.bisect_left(dp, i)] = i
    ans.append(dp.index(i) + 1)
lisLength = len(dp)
for i in range(len(arr) - 1, -1, -1):
    if ans[i] == lisLength:
        backtrace.append(arr[i])
        lisLength -= 1
print(N - (len(dp) - 1))
arr.sort()
for i in backtrace:
    arr.remove(i)
for i in arr:
    print(i)
