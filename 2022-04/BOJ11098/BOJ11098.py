# 11098번 첼시를 도와줘!
# https://www.acmicpc.net/problem/11098
import sys, os
sys.stdin = open('{}/BOJ11098.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
for _ in range(N):
    p=int(sys.stdin.readline())
    maxC=0
    for _ in range(p):
        C, name = sys.stdin.readline().split()
        C=int(C)
        tmp = max(maxC, C)
        if maxC != tmp:
            maxC=tmp
            ans = name
    print(ans)