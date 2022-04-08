import sys
def cal(a, b):
    A, B = a, b
    while a%b != 0:
        a, b = b, a%b
    return ((A*B) // b)

A, B = map(int,sys.stdin.readline().split())
N=cal(A,B)
print(A*B//N)
print(N)
