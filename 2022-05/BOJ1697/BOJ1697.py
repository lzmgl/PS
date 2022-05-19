# 1697번 숨바꼭질
# https://www.acmicpc.net/problem/1697
import sys, os
sys.stdin = open('{}/BOJ1697.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque
N, K=map(int,sys.stdin.readline().split())
board = [0 for _ in range(200000)]

q=deque([N])

while q:
    x=q.popleft()
    if x==K:
        break
    dx=[x-1, x+1, 2*x]
    for i in dx:
        if 0<=i<200000 and not board[i]:
            board[i]=board[x]+1
            q.append(i)
            
print(board[K])