# 1533번 길의 개수
# https://www.acmicpc.net/problem/1533
import sys, os
sys.stdin = open('{}/BOJ1533.txt'.format(os.path.dirname(os.path.realpath(__file__))))

mod = 1000003
N,S,E,T = map(int,input().split()); S -= 1; E -= 1
mat = [[0]*(5*N) for _ in range(5*N)]
for i in range(N):
    s = input()
    for j in range(4): mat[5*i+j+1][5*i+j] = 1
    for j in range(N):
        x = int(s[j])
        if x > 0: mat[i*5][j*5+x-1] = 1
        else: pass
def mul(A,B):
    C = [[0]*(5*N) for _ in range(5*N)]
    for i in range(5*N):
        for j in range(5*N):
            for k in range(5*N):
                C[i][j] += A[i][k]*B[k][j]
            C[i][j] %= mod
    return C
def power(A,n=T):
    if n == 1: return A
    ret = power(A, n//2)
    ret = mul(ret, ret)
    if n & 1: ret = mul(ret, A)
    return ret
print(power(mat)[S*5][E*5])