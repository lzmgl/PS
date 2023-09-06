# 10431번 줄세우기
# https://www.acmicpc.net/problem/10431
import sys, os
sys.stdin = open('{}/BOJ10431.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque
t=int(sys.stdin.readline())
for _ in range(t):
    ans=0
    data=list(map(int,sys.stdin.readline().split()))
    num, *data = data
    res=deque()
    for operator in data:
        isTaller=True
        for idx, operand in enumerate(res):
            if operator < operand:
                isTaller=False
                ans+=len(res)-idx
                res.insert(idx, operator)
                break
        if isTaller:
            res.append(operator)
    print(num, ans)