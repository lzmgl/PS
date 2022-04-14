# 13171번 A
# https://www.acmicpc.net/problem/13171
import sys, os
sys.stdin = open('{}/BOJ13171.txt'.format(os.path.dirname(os.path.realpath(__file__))))
A=int(sys.stdin.readline())
B=int(sys.stdin.readline())
print(pow(A,B,1000000007))