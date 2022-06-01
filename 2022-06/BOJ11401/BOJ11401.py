# 11401번 이항 계수 3
# 수학, 정수론, 조합론, 분할 정복을 이용한 거듭제곱, 모듈로 곱셈 역원, 페르마의 소정리
# https://www.acmicpc.net/problem/11401
import sys, os
sys.stdin = open('{}/BOJ11401.txt'.format(os.path.dirname(os.path.realpath(__file__))))
MOD = 1000000007

def get_factorial(n):
    if n==0:
        return 1
    for i in range(n-1, 1, -1):
        n = (n*i)%MOD
    return n

def fast_pow(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return (fast_pow(x, n//2) ** 2) % MOD
    else:
        return (fast_pow(x, n//2) ** 2 * x) % MOD

N, K = map(int, input().split())
A = get_factorial(N)
B = fast_pow(get_factorial(K), MOD-2)%MOD
C = fast_pow(get_factorial(N-K), MOD-2)%MOD
print(A*B*C%MOD)