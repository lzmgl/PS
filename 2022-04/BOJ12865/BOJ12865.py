# 12865번 평범한 배낭
# https://www.acmicpc.net/problem/12865
import sys, os
    
sys.stdin = open('{}/BOJ12865.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, K=map(int,sys.stdin.readline().split())
data=[]
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
print(data)