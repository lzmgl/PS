# 1075번 나누기
# https://www.acmicpc.net/problem/1075
import sys, os
sys.stdin = open('{}/BOJ1075.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
F=int(sys.stdin.readline())
S=N-(N%100)
for i in range(S, S+99):
    if not (i%F):
        print(f'{i%100:0>2}')
        exit()