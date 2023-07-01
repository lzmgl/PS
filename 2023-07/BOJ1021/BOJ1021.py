# 1021번 회전하는 큐
# https://www.acmicpc.net/problem/1021
import sys, os
sys.stdin = open('{}/BOJ1021.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque
N, M=map(int,sys.stdin.readline().split())
indexs = list(map(int,sys.stdin.readline().split()))
i=0
ans=0
deq=deque(list(range(1,N+1)))
for idx in indexs:
    while 1:
        if idx==deq[0]: #위치 = deque[0]
            deq.popleft()
            break
        else:
            if deq.index(idx)<len(deq)/2: # 왼쪽이면 rotate(-1)
                while deq[0]!=idx:
                    deq.rotate(-1)
                    ans+=1
            else:
                while deq[0]!=idx: # 오른쪽이면 rotate(-1)
                    deq.rotate(1)
                    ans+=1

print(ans)