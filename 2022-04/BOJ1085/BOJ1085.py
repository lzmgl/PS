# 1085번 직사각형에서 탈출
# https://www.acmicpc.net/problem/1085
import sys, os
    
sys.stdin = open('{}/BOJ1085.txt'.format(os.path.dirname(os.path.realpath(__file__))))
x,y,w,h=map(int,sys.stdin.readline().split())
print(min(min(abs(0-x), w-x),min(abs(0-y), h-y)))