# 9252번 LCS 2 backtrace lcs 최장공통부분수열
# https://www.acmicpc.net/problem/9252
import sys, os

sys.stdin = open("{}/BOJ9252.txt".format(os.path.dirname(os.path.realpath(__file__))))

s1 = [""] + list(sys.stdin.readline().strip())
s2 = [""] + list(sys.stdin.readline().strip())

lcs = [[0] * len(s2) for _ in range(len(s1))]
for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
j, i = len(s2) - 1, len(s1) - 1
ans = ""
while i > 0 and j > 0:
    if lcs[i][j] == lcs[i][j - 1]:
        j -= 1
    elif lcs[i][j] == lcs[i - 1][j]:
        i -= 1
    else:
        ans = s1[i] + ans
        i -= 1
        j -= 1
print(len(ans), ans, sep="\n")
