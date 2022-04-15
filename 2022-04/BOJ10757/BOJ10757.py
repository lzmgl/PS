# 10757번 큰 수 A+B
# https://www.acmicpc.net/problem/10757
import sys, os
    
sys.stdin = open('{}/BOJ10757.txt'.format(os.path.dirname(os.path.realpath(__file__))))
print(sum(map(int,input().split())))