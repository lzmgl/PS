# 1333번 부재중 전화
# https://www.acmicpc.net/problem/1333
import sys, os
sys.stdin = open('{}/BOJ1333.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, L, D=map(int, sys.stdin.readline().split())
t = 0
while(N):
    N -= 1
    t += L
    for i in range(5):
        if not t % D:
            if t < D:
                t = D
            print(t)
            exit()
        t += 1
# print(t)
# print(t%D)
# print(D-(t%D))
if t%D:
    t+=D-(t%D)
print(t)