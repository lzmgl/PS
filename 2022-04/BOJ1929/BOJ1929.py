# 1929번 소수 구하기
# https://www.acmicpc.net/problem/1929
import sys, os
sys.stdin = open('{}/BOJ1929.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 1929번 소수 구하기
# https://www.acmicpc.net/problem/1929
import sys
M, N= map(int, sys.stdin.readline().split())
is_primes = [True for i in range(1000001)] 
for i in range(2, N+1): 
    if is_primes[i]: 
        for j in range(i * i, N+1, i): 
            is_primes[j] = False
is_primes[0] = is_primes[1] = False

for i in range(M, N+1):
    if is_primes[i]:
        print(i)