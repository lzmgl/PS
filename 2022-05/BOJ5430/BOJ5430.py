# 5430번 AC
# list 공백없이 출력
# https://www.acmicpc.net/problem/5430
import sys, os
sys.stdin = open('{}/BOJ5430.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import deque
T=int(sys.stdin.readline())
for _ in range(T):
    p=sys.stdin.readline().rstrip()
    n=int(sys.stdin.readline())
    arr=deque(eval(sys.stdin.readline().strip()))
    p=p.replace('RR', '')
    isR=1
    for c in p:
        if c == 'R':
            isR*=-1
        else:
            try:
                if isR>0:
                    arr.popleft()
                else:
                    arr.pop()
            except:
                print('error')
                break
    else:
        if isR<0:
            (arr.reverse())
        print(str(list(arr)).replace(' ',''))