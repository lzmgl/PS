# 1978번 소수 찾기
# https://www.acmicpc.net/problem/1978
import sys, os
sys.stdin = open('{}/BOJ1978.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 403 Forbidden
# https://www.acmicpc.net/problem/1978

import sys
N=int(sys.stdin.readline())
number=list(map(int, sys.stdin.readline().split()))
for item in number:
    if item<2:
        N-=1
        continue
    for i in range(2,item):
        if item%i==0:
            N-=1
            break
sys.stdout.write(str(N))
'''
import sys; 
is_primes = [True for i in range(1001)] 
for i in range(2, 1001): 
    if is_primes[i]: 
        for j in range(i * i, 1001, i): 
            is_primes[j] = False
is_primes[0] = is_primes[1] = False 
Ans = 0 
N = int(sys.stdin.readline()) 
inputs = sys.stdin.readline().split(' ') 
for i in inputs: 
    if is_primes[int(i)]: 
        Ans += 1 
sys.stdout.write(str(Ans))
'''