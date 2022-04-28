# 2869번 달팽이는 올라가고 싶다
# https://www.acmicpc.net/problem/2869
import sys, os
sys.stdin = open('{}/BOJ2869.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import math
A, B, V=map(int,sys.stdin.readline().split())
h=V-A
cnt=math.ceil(h/(A-B))
print(cnt+1)