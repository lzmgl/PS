# 1074번 Z
# https://www.acmicpc.net/problem/1074
import sys, os
sys.stdin = open('{}/BOJ1074.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, r, c=map(int,sys.stdin.readline().split())
cnt=0
while N>0:
    rag = pow(2, 2*(N-1))
    M=pow(2,N)
    if r < M//2:
        if c < M//2: #좌상 (x+0, y +0)
            cnt+=rag*0
        else:#우상 (x+dx, y+0)
            cnt+=rag*1
            c-=pow(2,N-1)
    else:
        if c < M//2: #좌하 (x=0, y=dy)
            cnt+=rag*2
            r-=pow(2,N-1)
        else:#우하 (x+dx, y+dy)
            cnt+=rag*3
            r-=pow(2,N-1)
            c-=pow(2,N-1)
    N-=1
if r==0:
    if c==0:
        cnt+=0
    else:
        cnt+=1
else:
    if c==0:
        cnt+=2
    else:
        cnt+=3
print(cnt)