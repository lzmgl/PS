# 1934번 최소공배수
# https://www.acmicpc.net/problem/1934
import sys, os
sys.stdin = open('{}/BOJ1934.txt'.format(os.path.dirname(os.path.realpath(__file__))))
def cal(a, b):
    A, B = a, b
    while a%b != 0:
        a, b = b, a%b
    print((A*B) // b)
for _ in[0]*int(input()):
    A, B = map(int,sys.stdin.readline().split())
    cal(A,B)
    