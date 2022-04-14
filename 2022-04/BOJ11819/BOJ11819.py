# 11819번 The Shortest does not Mean the Simplest
# https://www.acmicpc.net/problem/11819
import sys, os
    
sys.stdin = open('{}/BOJ11819.txt'.format(os.path.dirname(os.path.realpath(__file__))))
A,B,C=map(int,sys.stdin.readline().split())
print(pow(A,B,C))