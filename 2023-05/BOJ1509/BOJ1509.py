# 1509번 팰린드롬 분할
# https://www.acmicpc.net/problem/1509
import sys, os
sys.stdin = open('{}/BOJ1509.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import math
data=sys.stdin.readline().strip()
ans=[]
L=len(data)

dp = [2500 for _ in range(L + 1)]
dp[-1] = 0
is_p = [[0 for j in range(L)] for i in range(L)]
def pelCheck(left, right):
    ret=is_p[left][right]
    if not ret:
        return ret
    if left==right:
        is_p[left][right]=1
        return 1
    if data[left] == data[right]:
        if left+1==right:
            is_p[left][right]=1
            return pelCheck(left+1, right-1)

def DP(start):
    ret=dp[start]
    if not ret:
        return ret
    if start==L:
        return 0
    ret=math.inf
    for i in range(start, L):
        if pelCheck()
        