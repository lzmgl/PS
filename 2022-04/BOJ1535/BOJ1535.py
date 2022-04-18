# 1535번 안녕
# knapsack DP
# https://www.acmicpc.net/problem/1535
import sys, os
    
sys.stdin = open('{}/BOJ1535.txt'.format(os.path.dirname(os.path.realpath(__file__))))



N=int(sys.stdin.readline())
L = list(map(int,sys.stdin.readline().split()))
J = list(map(int,sys.stdin.readline().split()))
capacity=100

DP = [[-1 for i in range(capacity+1)] for _ in range(N)]

def knapsack(idx, cap):
    if idx==N:
        return 0
    ret=DP[idx][cap]
    if ret != -1:
        return ret
    if L[idx]<cap:
        ret=knapsack(idx+1, cap-L[idx])+J[idx]
    ret = max(ret, knapsack(idx+1, cap))
    DP[idx][cap]=ret
    return ret

print(knapsack(0,capacity))