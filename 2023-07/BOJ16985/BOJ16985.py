# 16985번 Maaaaaaaaaze
# https://www.acmicpc.net/problem/16985
import sys, os
sys.stdin = open('{}/BOJ16985.txt'.format(os.path.dirname(os.path.realpath(__file__))))
M, N, H=5,5,5
for z in range(H):
    for y in range(N):
        for x in range(M):
            