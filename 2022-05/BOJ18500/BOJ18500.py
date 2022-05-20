# 18500번 미네랄 2
# https://www.acmicpc.net/problem/18500
import sys, os
sys.stdin = open('{}/BOJ18500.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque
R, C=map(int,sys.stdin.readline().split())
cave=[]
for _ in range(R):
    cave.append(sys.stdin.readline().strip())
N=int(sys.stdin.readline())
height=[]
for _ in range(N):
    height.append(int(sys.stdin.readline()))
    
dy=[0,0,1,-1]
dx=[1,-1,0,0]
# 마지막이 위, 앞 3개 확인 요망.
q=deque()
for i, c in enumerate(height):
    if i%2 == 0:
        for idx in range(R):
            data=cave[R-c][idx]
            if data=='x':
                cave[R-c][idx]='.'
                q.append([idx, R-c])
                break
    else:
        for idx in range(R-1, -1, -1):
            data=cave[R-c][idx]
            if data=='x':
                cave[R-c][idx]='.'
                q.append([idx, R-c])
                break
        
    while q:
        x, y = q.popleft()
        for i in range(3): #양옆, 밑 체크
            nx, ny = x+dx, y+dy
            if C > nx >= 0 and R > ny >= 0:
                d