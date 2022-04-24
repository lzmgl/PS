# 1152번 단어의 개수
# https://www.acmicpc.net/problem/1152
import sys, os
sys.stdin = open('{}/BOJ1152.txt'.format(os.path.dirname(os.path.realpath(__file__))))
print(len(input().split()))
