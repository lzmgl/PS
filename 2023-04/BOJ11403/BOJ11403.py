# 11403번 경로 찾기
# https://www.acmicpc.net/problem/11403
import sys, os
sys.stdin = open('{}/BOJ11403.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N = int(sys.stdin.readline().strip())
net=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if net[i][j]==0:
            net[i][j]=999
for k in range(N):
    for i in range(N):
        for j in range(N):
            net[i][j]=min(net[i][j], net[i][k]+net[k][j])

for i in range(N):
    for j in range(N):
        if net[i][j]==999:
            net[i][j]=0
        else:
            net[i][j]=1
for item in net:
    for j in item:
        print(j, end=' ')
    print()