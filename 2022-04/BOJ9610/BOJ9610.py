# 9610번 사분면
# https://www.acmicpc.net/problem/9610
import sys, os
sys.stdin = open('{}/BOJ9610.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())import sys
side = {'Q1':0, 'Q2':0, 'Q3':0, 'Q4':0, 'AXIS':0}
N=int(sys.stdin.readline())
for _ in range(N):
    x,y=map(int, sys.stdin.readline().split())
    if x>0:
        if y>0:
            side['Q1']+=1
        elif y<0:
            side['Q4']+=1
        else:
            side['AXIS']+=1
    elif x<0:
        if y>0:
            side['Q2']+=1
        elif y<0:
            side['Q3']+=1
        else:
            side['AXIS']+=1
    else:
        side['AXIS']+=1
for key, value in side.items():
    print(key+': '+str(value))