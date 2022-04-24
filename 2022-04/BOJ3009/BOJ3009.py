# 3009번 네 번째 점
# https://www.acmicpc.net/problem/3009
import sys, os
sys.stdin = open('{}/BOJ3009.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())import sys
x=0
y=0
for i in range(3):
    a1, b1 = map(int,sys.stdin.readline().split())
    x^=a1
    y^=b1
print(x,y)