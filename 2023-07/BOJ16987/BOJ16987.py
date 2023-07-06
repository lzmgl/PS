# 16987번 계란으로 계란치기
# https://www.acmicpc.net/problem/16987
import sys, os
sys.stdin = open('{}/BOJ16987.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
data=[]
for _ in range(N):
    s, w = map(int, sys.stdin.readline().split())
    data.append([s,w])
answer=0

def egg(idx, eggs):
    global answer
    if idx==N:
        cnt=0
        print(eggs)
        for i in range(N):
            if eggs[i][0]<1:
                cnt+=1
        if cnt>answer:
            answer=cnt
        return 
    if eggs[idx][0]>0:
        for i in range(N):
            br=False
            if i!=idx and eggs[i][0]>0:
                br=True
                tmp=(eggs[:])
                tmp[i][0]-=eggs[idx][1]
                tmp[idx][0]-=eggs[i][1]
                egg(idx+1, tmp)
        if not br:
            egg(idx+1, eggs)
    else:
        egg(idx+1, eggs)

egg(0, data)
print(answer)