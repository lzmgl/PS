# 2338번 긴자리 계산
# https://www.acmicpc.net/problem/2338
import sys, os
    
sys.stdin = open('{}/BOJ2338.txt'.format(os.path.dirname(os.path.realpath(__file__))))
A=int(sys.stdin.readline())
B=int(sys.stdin.readline())
print(A+B)
print(A-B)
print(A*B)