# 14440번 정수 수열
# 미해결
# https://www.acmicpc.net/problem/14440
import sys, os
    
sys.stdin = open('{}/BOJ14440.txt'.format(os.path.dirname(os.path.realpath(__file__))))
x,y,a0,a1,n=map(int, sys.stdin.readline().split())
for i in range(n - 1):
    a2 = (a0 * y + a1 * x) % 100
    a0 = a1
    a1 = a2
if n == 0:
    a2 = a0
if n == 1: a2 = a1
print(f'{a2:02d}')
# Fibo=[a0,a1]
# i=2
# p=-1
# isTrue=False
# while True:
#     a1, a0=(x*Fibo[i-1]+y*Fibo[i-2])%100, a1
#     Fibo.append((x*Fibo[i-1]+y*Fibo[i-2])%100)
#     if Fibo[i-1]==Fibo[2] and Fibo[i-2]==Fibo[1]:
#         if isTrue:
#             break
#         isTrue=True
#     p+=1
#     i+=1
# res=Fibo[N%p]
# print(f'{res:02d}')
# def pisano(m):
#     f0=0
#     f1=1
#     f2=f0+f1
    
#     for i in range(m*m):
#         f2=(f0+f1)%m
#         f0=f1
#         f1=f2
#         if f0==0 and f1==1:
#             return i+1
    
# print(pisano(100))