# 1271번 엄청난 부자2
# https://www.acmicpc.net/problem/1271
import sys, os
    
sys.stdin = open('{}/BOJ1271.txt'.format(os.path.dirname(os.path.realpath(__file__))))
A,B=(map(int, sys.stdin.readline().split()))
print(A//B)
print(A%B)