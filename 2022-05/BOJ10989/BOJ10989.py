# 10989번 수 정렬하기 3
# https://www.acmicpc.net/problem/10989
import sys, os
sys.stdin = open('{}/BOJ10989.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
data=[0]*10001
for _ in range(N):
    data[int(sys.stdin.readline())]+=1
for i in range(1,10001):
    if data[i]>0:
        for cnt in range(data[i]):
            print(i)