# 16985번 Maaaaaaaaaze
# https://www.acmicpc.net/problem/16985
# https://velog.io/@emplam27/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%EA%B9%8A%EC%9D%80%EB%B3%B5%EC%82%AC%EB%8A%94-deepcopy%EA%B0%80-%EB%B9%A0%EB%A5%BC%EA%B9%8C-slicing%EC%9D%B4-%EB%B9%A0%EB%A5%BC%EA%B9%8C 딥카피 하면 느린 이유
import sys, os
sys.stdin = open('{}/BOJ16985.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import copy
from itertools import permutations
from collections import deque
M, N, H=5,5,5
data1=[]
dx=[0,0,0,0,1,-1]
dy=[0,0,1,-1,0,0]
dz=[1,-1,0,0,0,0]
def rotate_90(arr):
    tmp=[[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            tmp[i][j]=arr[j][4-i]
    return tmp

for z in range(H):
    plate=[]
    for y in range(N):
        tmp=list(map(int,sys.stdin.readline().split()))
        plate.append(tmp)
    data1.append(plate)


def bfs():
    q=deque()
    cnt=0
    q.append((0,0,0,cnt))
    visited=[[[0]*5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0]=1
    while q:
        z,y,x,cnt = q.popleft()
        if z==4 and y == 4 and x == 4:
            return cnt
        for i in range(6):
            nz, ny, nx = z+dz[i], y+dy[i], x+dx[i]
            if 0<=nz<5 and  0<=ny<5 and  0<=nx<5 and visited[nz][ny][nx]==0:
                if data[nz][ny][nx]==1:
                    visited[nz][ny][nx]=visited[z][y][x]+1
                    q.append((nz,ny,nx,cnt+1))
    return -1

minC=float(1e9)
per = list(permutations([0,1,2,3,4],5))

# 각 plate를 쌓는 순열 120가지
# 4(회전수)**5(plate) 경우의수 브루트포스
for i in range(len(per)):
    data=copy.deepcopy(data1)   #deepcopy 안쓰는 방법..
    for j in range(5):
        data[j]=data1[per[i][j]]
    for _ in range(4):
        data[0]=rotate_90(data[0])
        for _ in range(4):
            data[1]=rotate_90(data[1])
            for _ in range(4):
                data[2]=rotate_90(data[2])
                for _ in range(4):
                    data[3]=rotate_90(data[3])
                    for _ in range(4):
                        data[4]=rotate_90(data[4])
                        if data[0][0][0]==1 and data[4][4][4]==1: 
                            ans=bfs()
                            if ans==12:
                                print(12)
                                exit()
                            if ans!=-1:
                                minC=min(minC, ans)
                        else: #입구 출구 없는경우
                            continue
                                
if minC==float(1e9):
    print(-1)
else:
    print(minC)