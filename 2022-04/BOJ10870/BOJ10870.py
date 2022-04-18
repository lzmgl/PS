# 10870번 피보나치 수 5
# https://www.acmicpc.net/problem/10870
import sys, os
    
sys.stdin = open('{}/BOJ10870.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())

fibo=[0,1]
for i in range(2,N+1):
    fibo.append(fibo[i-1]+fibo[i-2])
print(fibo[N])