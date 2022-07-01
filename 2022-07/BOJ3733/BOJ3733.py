# 3733번 Shares
# https://www.acmicpc.net/problem/3733
import sys, os
sys.stdin = open('{}/BOJ3733.txt'.format(os.path.dirname(os.path.realpath(__file__))))
for line in sys.stdin:
    N, S=map(int, line.split())
    print(S//(N+1))