# 10797번 10부제
# https://www.acmicpc.net/problem/10797
import sys, os
sys.stdin = open('{}/BOJ10797.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().split()))
print(numbers.count(N))
'''
k=input()
print(input().count(k))
'''