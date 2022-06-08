# 9251번 LCS
# DP
# https://www.acmicpc.net/problem/9251
import sys, os
sys.stdin = open('{}/BOJ9251.txt'.format(os.path.dirname(os.path.realpath(__file__))))
s1=sys.stdin.readline().strip()
s2=sys.stdin.readline().strip()
maxlen=max(len(s1), len(s2))+1
lcs=[[0]*maxlen for _ in range(maxlen)]
for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1]==s2[j-1]:
            lcs[i][j]=lcs[i-1][j-1]+1
        else:
            lcs[i][j]=max(lcs[i-1][j], lcs[i][j-1])
print(max(map(max, lcs)))