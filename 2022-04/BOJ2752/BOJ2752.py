# 2752번 세수정렬
# https://www.acmicpc.net/problem/2752
import sys, os
sys.stdin = open('{}/BOJ2752.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2752번 세수정렬
# https://www.acmicpc.net/problem/2752
import sys
data=list(map(int, sys.stdin.readline().split()))
data.sort()
print(*data)
