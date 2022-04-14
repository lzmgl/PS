# 2749번 피보나치 수 3
# https://www.acmicpc.net/problem/2749
import sys, os
    
sys.stdin = open('{}/BOJ2749.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
Fibo=[0,1]
i=1
while i!=15*10**5:
    i+=1
    Fibo.append((Fibo[i-1]+Fibo[i-2])%1000000)
    if Fibo[i] == 1:
        if Fibo[i-1] == 0:
            break
print(Fibo[N%(15*10**5)])