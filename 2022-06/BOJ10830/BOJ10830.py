# 10830번 행렬 제곱
# https://www.acmicpc.net/problem/10830
import sys, os
from operator import matmul
sys.stdin = open('{}/BOJ10830.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, B=map(int,sys.stdin.readline().split())
data=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]

mod=1000

def matMul(a, b):
    global mod
    n=len(a)
    data = [[0 for i in range(len(a))] for _ in range(len(a))]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                data[i][j]+=(a[i][k]*b[k][j])
            data[i][j]%=mod
    return data

def DFS(arr, B):
    if B == 1:
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                arr[i][j] %= 1000
        return arr
    
    tmp = DFS(arr, B//2)
    print(tmp)
    
    if B % 2 != 0:
        return matMul(matMul(tmp, tmp), arr)
    else:
        return matMul(tmp, tmp)

ans = DFS(data, B)
for i in ans:
    print(*i)