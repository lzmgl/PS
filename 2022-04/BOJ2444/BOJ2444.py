# 2444번 별 찍기 - 7
# https://www.acmicpc.net/problem/2444
import sys, os
sys.stdin = open('{}/BOJ2444.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 2444번 별 찍기 - 7
# https://www.acmicpc.net/problem/2444
'''
N=int(input())
for i in range(1,N): 
    print(' '*(N-i), '*'*((i*2)-1), sep='')
for i in range(N,0,-1): 
    print(' '*(N-i), '*'*((i*2)-1), sep='')
'''
N=int(input())
for i in range(-N+1,N): 
    i=abs(i)
    print(' '*(i), '*'*(2*(N-i)-1), sep='')