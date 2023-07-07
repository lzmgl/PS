# 16987번 계란으로 계란치기
# https://www.acmicpc.net/problem/16987
import sys, os
sys.stdin = open('{}/BOJ16987.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
list_s=[]
list_w=[]
# data=[]
for _ in range(N):
    s, w = map(int, sys.stdin.readline().strip().split())
    list_s.append(s)
    list_w.append(w)
    # data.append([s,w])
    # 2차원 deepcopy를 slicing으로 안돼서 수정함. how
answer=0

def egg(idx, eggs):
    global answer
    if idx==N: # 마지막계란이면 깨진거 계산(각 경우 다 계산해서 젤 많은거)
        cnt=0
        for i in range(N):
            if eggs[i]<=0:
                cnt+=1
        if cnt>answer:
            answer=cnt
        return 
    if eggs[idx]>0: #든 계란이 안깨진거면
        br=False #깰수있는 계란 체크
        for i in range(N):
            if i!=idx and eggs[i]>0:
                br=True
                tmp=eggs[:] #깬 경우 복사해서 넘겨주기
                tmp[i]-=list_w[idx]
                tmp[idx]-=list_w[i]
                egg(idx+1,tmp)
        if not br: #깰수있는 계란이 없으니까 N으로 바로 넘겨
            egg(N,eggs)
    else: #깨진계란들면 넘기기
        egg(idx+1,eggs)

egg(0, list_s)
print(answer)