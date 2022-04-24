# 10984번 내 학점을 구해줘
# https://www.acmicpc.net/problem/10984
import sys, os
sys.stdin = open('{}/BOJ10984.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T=int(sys.stdin.readline())
for _ in range(T):
    sumC=0
    sumG=0
    N=int(sys.stdin.readline())
    for _ in range(N):
        C, G = sys.stdin.readline().split()
        sumC+=int(C)
        sumG+=float(G)*int(C)
    print(sumC,round(sumG/sumC, 1))