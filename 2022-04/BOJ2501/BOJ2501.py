# 2501번 약수 구하기
# https://www.acmicpc.net/problem/2501
import sys, os
sys.stdin = open('{}/BOJ2501.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2501번 약수 구하기
# https://www.acmicpc.net/problem/2501
import sys
N, K=map(int, sys.stdin.readline().rstrip().split())
res=[]
for i in range(1,N+1):
    if N%i==0:
        res.append(i)
try:
    print(res[K-1])
except:
    print(0)
