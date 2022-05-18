# 1193�� �м�ã��
# https://www.acmicpc.net/problem/1193
from re import I
import sys, os
sys.stdin = open('{}/BOJ1193.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
i=0
cnt=0
while N>cnt:
    i+=1
    cnt+=i
cnt-=i
if i%2!=0:
    y=i+1
    for x in range(1, i+1):
        cnt+=1
        y-=1
        if cnt==N:
            print(f'{y}/{x}')
            exit()
else:
    x=i+1
    for y in range(1, i+1):
        cnt+=1
        x-=1
        if cnt==N:
            print(f'{y}/{x}')
            exit()