# 2163번 초콜릿 자르기
# https://www.acmicpc.net/problem/2163
import sys, os
sys.stdin = open('{}/BOJ2163.txt'.format(os.path.dirname(os.path.realpath(__file__))))
a, c = sys.stdin.readline().rsplit()
print(int(a)*int(c)-1)