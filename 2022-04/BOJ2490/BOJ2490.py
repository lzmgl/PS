# 2490번 윷놀이
# https://www.acmicpc.net/problem/2490
import sys, os
sys.stdin = open('{}/BOJ2490.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2490번 윷놀이
# https://www.acmicpc.net/problem/2490
import sys
dic={0:'D', 4:'E', 3:'A', 2:'B', 1:'C'}
for _ in range(3):
    tmp=list(map(int,sys.stdin.readline().split()))
    print(dic[sum(tmp)])