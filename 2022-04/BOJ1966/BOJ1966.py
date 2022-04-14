# 1966번 프린터 큐
# https://www.acmicpc.net/problem/1966
import sys, os
sys.stdin = open('{}/BOJ1966.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T=int(sys.stdin.readline())
for _ in range(T):
    idrr=[]
    N, M = map(int, sys.stdin.readline().split())
    tmp = list(map(int, (sys.stdin.readline().split())))
    v=tmp[M]
    for i in range(N):
        if i!=M:
            idrr.append([tmp[i], 0])
        else:
            idrr.append([tmp[i], 1])
    cnt=1
    while True:
        idx=tmp.index(max(tmp))
        idrr = (idrr[idx:]+idrr[:idx])
        tmp = (tmp[idx:]+tmp[:idx])
        if idrr[0][0] == v:
            if idrr[0][1]==1:
                break
        idrr.pop(0)
        tmp.pop(0)
        cnt+=1
    print(cnt)