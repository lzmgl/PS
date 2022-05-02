# 15829번 Hashing
# https://www.acmicpc.net/problem/15829
import sys, os
sys.stdin = open('{}/BOJ15829.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import string
num=1234567891
alp=[0]
alp2 = list(string.ascii_lowercase)
alp+=alp2
N=int(sys.stdin.readline())
s=sys.stdin.readline().rstrip()
d=0
for idx,c in enumerate(s):
    d+=(alp.index(c)*pow(31,idx))
print(d%num)