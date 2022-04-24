# 2908번 상수
# https://www.acmicpc.net/problem/2908
import sys, os
sys.stdin = open('{}/BOJ2908.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2908번 상수
# https://www.acmicpc.net/problem/2908
import sys
a, b=sys.stdin.readline().split()
a=a[::-1]
b=b[::-1]
print(max(int(a),int(b)))