# 2576번 홀수
# https://www.acmicpc.net/problem/2576
import sys, os
sys.stdin = open('{}/BOJ2576.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2576번
# https://www.acmicpc.net/problem/2576
import sys
sumN=0
minN=9999
for i in range(7):
    tmp=int(sys.stdin.readline())
    if tmp%2!=0:
        sumN+=tmp
        minN=min(minN,tmp)
if minN>100:
    print(-1)
    exit()
print(sumN)
print(minN)