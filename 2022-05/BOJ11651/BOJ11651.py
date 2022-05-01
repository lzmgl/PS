# 11651번 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651
import sys, os
sys.stdin = open('{}/BOJ11651.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
data=[]
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    data.append(tmp)
data.sort()
data.sort(key=lambda x : x[1])
for item in data:
    print(*item)