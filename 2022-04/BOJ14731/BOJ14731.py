# 14731번 謎紛芥索紀 (Large)
# https://www.acmicpc.net/problem/14731
import sys, os
    
sys.stdin = open('{}/BOJ14731.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
data=[]
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
res=0
for c, k in data:
    res+=c*k*pow(2,k-1,1000000007)
print(res)