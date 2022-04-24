# 4153번 직각삼각형
# https://www.acmicpc.net/problem/4153
import sys, os
sys.stdin = open('{}/BOJ4153.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 4153번 직각삼각형
# https://www.acmicpc.net/problem/4153
import sys
while (s:=input())>'0 0 0':
    data=[]
    data=list(map(int, s.split()))
    data.sort()
    if data[0]**2+data[1]**2 == data[2]**2:
        print('right')
    else:
        print('wrong')