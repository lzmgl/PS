# 9019번 DSLR
# https://www.acmicpc.net/problem/9019
import sys, os
sys.stdin = open('{}/BOJ9019.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque
def D(n):
    return (2*n)%10000
def S(n):
    return (n+9999)%10000
def L(n):
    a, b = divmod(n, 1000)
    return (b*10)+a
def R(n):
    a, b = divmod(n, 10)
    return (b*1000)+a
ans=[[0]*4 for _ in range(10000)]

for i in range(10000):
    ans[i][0]=D(i)
    ans[i][1]=S(i)
    ans[i][2]=L(i)
    ans[i][3]=R(i)

T=int(sys.stdin.readline())

func=['D', 'S', 'L', 'R']

for _ in range(T):
    visited=[-1]*10000
    a, b = map(int, sys.stdin.readline().split())
    q=deque()
    q.append([a, ''])
    visited[a]=1
    while q:
        num, acc = q.popleft()
        if num==b:
            print(acc)
            break
        for j in range(4):
            if visited[ans[num][j]]==1:
                continue
            visited[ans[num][j]]=1
            q.append([ans[num][j], acc+func[j]])
