# 2609번 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609
import sys, os
sys.stdin = open('{}/BOJ2609.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())import sys
def cal(a, b):
    A, B = a, b
    while a%b != 0:
        a, b = b, a%b
    return ((A*B) // b)

A, B = map(int,sys.stdin.readline().split())
N=cal(A,B)
print(A*B//N)
print(N)
