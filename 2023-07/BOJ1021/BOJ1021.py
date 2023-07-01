# 1021번 회전하는 큐
# https://www.acmicpc.net/problem/1021
import sys, os
sys.stdin = open('{}/BOJ1021.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque
N, M=map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
i=0
ans=0
deq=deque(list(range(1,N+1)))
for item in data:
    while 1:
        if item==deq[0]:
            deq.popleft()
            break
        else:
            if deq.index(item)<len(deq)/2:
                while deq[0]!=item:
                    deq.rotate(-1)
                    ans+=1
            else:
                while deq[0]!=item:
                    deq.rotate(1)
                    ans+=1

print(ans)