# 2660번 회장뽑기 플로이드
# https://www.acmicpc.net/problem/2660
import sys, os
sys.stdin = open('{}/BOJ2660.txt'.format(os.path.dirname(os.path.realpath(__file__))))

N=int(sys.stdin.readline())
adj = [[float('inf')]*(N+1) for _ in range(N+1)]
while 1:
    a, b = map(int,sys.stdin.readline().split())
    if a==-1 and b==-1:
        break
    adj[a][b]=1
    adj[b][a]=1

for i in range(N+1):
    for j in range(N+1):
        if i==j:
            adj[i][j]=0

ans=[0]*(N+1)
for k in range(1,N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])

for i in range(1, N+1):
    ans[i]=max(adj[i][1:])
    
answer=[]
res = (min(ans[1:]))
for i in range(N+1):
    if ans[i] == res:
        answer.append(i)
print(res, len(answer))
print(*answer)