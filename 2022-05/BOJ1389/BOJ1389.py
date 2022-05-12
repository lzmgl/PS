# 1389번 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389
import sys, os
sys.stdin = open('{}/BOJ1389.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, M=map(int, sys.stdin.readline().split())
net = [[5001]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if i==j:
            net[i][j]=0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    net[a][b]=1
    net[b][a]=1
    
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            net[i][j]=min(net[i][j], net[i][k]+net[k][j])

minN=99999999
for idx, item in enumerate(net):
    tmp=min(minN, sum(item))
    if minN!=tmp:
        mini=idx
        minN=tmp
print(mini)