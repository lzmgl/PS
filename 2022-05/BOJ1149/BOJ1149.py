# 1149번 RGB거리
# DP, top down, TOPDOWN
# https://www.acmicpc.net/problem/1149
import sys, os
sys.stdin = open('{}/BOJ1149.txt'.format(os.path.dirname(os.path.realpath(__file__))))
sys.setrecursionlimit(100001)
N=int(sys.stdin.readline())
rgb = [[int(x) for x in sys.stdin.readline().split()] for i in range(N)]

def dp(lev):
    if lev == -1:
        return [0,0,0]
    cache = dp(lev-1)
    rgb[lev][0] += min(cache[1], cache[2])
    rgb[lev][1] += min(cache[0], cache[2])
    rgb[lev][2] += min(cache[0], cache[1])
    return rgb[lev]

print(min(dp(N-1)))