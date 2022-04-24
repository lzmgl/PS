# 5063번 TGN
# https://www.acmicpc.net/problem/5063
import sys, os
sys.stdin = open('{}/BOJ5063.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())import sys
N=int(sys.stdin.readline())
for _ in range(N):
    r,e,c = map(int,sys.stdin.readline().split())
    if e-c>r:
        print("advertise")
    elif e-c<r:
        print("do not advertise")
    elif e-c==r:
        print("does not matter")
