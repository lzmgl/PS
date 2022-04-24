# 10569번 다면체
# https://www.acmicpc.net/problem/10569
import sys, os
sys.stdin = open('{}/BOJ10569.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
for i in range(N):
    V, E = map(int, sys.stdin.readline().split())
    print(2-V+E)