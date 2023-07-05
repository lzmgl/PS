# 5427번 불
# https://www.acmicpc.net/problem/5427
import sys, os
sys.stdin = open('{}/BOJ5427.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T=int(sys.stdin.readline().strip())
for _ in range(T):
    data=[]
    w, h=map(int, sys.stdin.readline().strip().split)
    for _ in range(h):
        data.append(sys.stdin.readline().strip())
    print(data)