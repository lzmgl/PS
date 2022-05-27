# 1992번 쿼드트리
# https://www.acmicpc.net/problem/1992
import sys, os
sys.stdin = open('{}/BOJ1992.txt'.format(os.path.dirname(os.path.realpath(__file__))))
sys.setrecursionlimit(100000)
N=int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(N)]

def solve(length, r, c):
    global N
    L=length//2
    if length==1:
        return data[r][c]
    up_left = solve(L, r, c)
    up_right = solve(L, r, c+L)
    down_left = solve(L, r+L, c)
    down_right = solve(L, r+L, c+L)
    if up_left == up_right == down_left == down_right and len(up_left)==1:
        if L==N:
            return "("+up_left+")"
        else:
            return up_left
    else:
        return "("+up_left+up_right+down_left+down_right+")"

print(solve(N, 0, 0))