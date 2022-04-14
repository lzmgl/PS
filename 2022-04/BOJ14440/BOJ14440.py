# 14440번 정수 수열
# 미해결
# https://www.acmicpc.net/problem/14440
import sys, os
    
sys.stdin = open('{}/BOJ14440.txt'.format(os.path.dirname(os.path.realpath(__file__))))
x,y,a0,a1,N=map(int, sys.stdin.readline().split())
Fibo=[a0,a1]
i=1
while i!=15*10:
    i+=1
    Fibo.append((x*Fibo[i-1]+y*Fibo[i-2])%100)
res=Fibo[N%(15*10)]
print(i)
print(Fibo)
print(f'{res:02d}')