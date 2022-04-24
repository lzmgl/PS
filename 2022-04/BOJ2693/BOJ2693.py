# 2693번 N번째 큰 수
# https://www.acmicpc.net/problem/2693
import sys, os
sys.stdin = open('{}/BOJ2693.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
for _ in range(N):
    data=list(map(int, sys.stdin.readline().split()))
    data.sort()
    print(data[7])