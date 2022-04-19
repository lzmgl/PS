# 12865번 평범한 배낭
# https://www.acmicpc.net/problem/12865
import sys, os
    
sys.stdin = open('{}/BOJ12865.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, capacity=map(int,sys.stdin.readline().split())

data=[]
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
    

DP = [[-1 for i in range(capacity+1)] for _ in range(N)]

def knapsack(idx, cap):
    if idx==N:
        return 0
    ret=DP[idx][cap]
    if ret != -1:
        return ret
    if data[idx][0]<=cap:
        ret=knapsack(idx+1, cap-data[idx][0])+data[idx][1]
    ret = max(ret, knapsack(idx+1, cap))
    DP[idx][cap]=ret
    return ret

print(knapsack(0,capacity))


