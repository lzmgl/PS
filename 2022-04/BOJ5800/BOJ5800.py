# 5800번 성적 통계
# https://www.acmicpc.net/problem/5800
import sys, os
sys.stdin = open('{}/BOJ5800.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
for i in range(1, N+1):
    tmp=list(map(int, sys.stdin.readline().split()))
    tmp=tmp[1:]
    tmp.sort()
    maxN, minN=max(tmp), min(tmp)
    gap=0
    for idx in range(len(tmp)-1):
        gap=max(tmp[idx+1]-tmp[idx], gap)
    print(f'Class {i}')
    print(f'Max {maxN}, Min {minN}, Largest gap {gap}')