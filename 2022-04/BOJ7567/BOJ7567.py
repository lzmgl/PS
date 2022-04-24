# 7567번 그릇
# https://www.acmicpc.net/problem/7567
import sys, os
sys.stdin = open('{}/BOJ7567.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())a=input()
tmp=''
res=0
for item in a:
    if item==tmp:
        res+=5
    else:
        res+=10
        tmp=item
print(res)