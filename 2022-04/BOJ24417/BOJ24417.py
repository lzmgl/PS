# 24417번 알고리즘 수업 - 피보나치 수 2
# https://www.acmicpc.net/problem/24417
import sys, os
    
sys.stdin = open('{}/BOJ24417.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
mod=1000000007

f=[0]*(N+1)
cnt2=0
def fibonacci(n) :
    global cnt2
    f[1]=f[2]=1
    for i in range(3,n+1):
        cnt2+=1
        cnt2%=mod
        f[i] = f[i-1] + f[i-2];  # 코드2
    return f[n];
def matMul(a, b):
    global mod
    n=len(a)
    data=[[0,0],[0,0]]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                data[i][j]= data[i][j]+(a[i][k]*b[k][j])
            data[i][j]%=mod
    return data
            
matAns=[[1,0], [0,1]]
matFibo=[[1,1], [1,0]]

fibonacci(N)
while N>0:
    if N%2==1:
        matAns=matMul(matAns,matFibo)
    matFibo=matMul(matFibo,matFibo)
    N//=2

print(matAns[0][1], cnt2)