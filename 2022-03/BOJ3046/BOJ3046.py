# 3046번 R2
# https://www.acmicpc.net/problem/3046
import sys, os
sys.stdin = open('{}/BOJ3046.txt'.format(os.path.dirname(os.path.realpath(__file__))))
a, c = sys.stdin.readline().rsplit()
print(2*int(c)-int(a))