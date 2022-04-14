# 1629번 곱셈
# https://www.acmicpc.net/problem/1629
import sys, os
    
sys.stdin = open('{}/BOJ1629.txt'.format(os.path.dirname(os.path.realpath(__file__))))
A,B,C=map(int,sys.stdin.readline().split())

print(pow(A,B,C))