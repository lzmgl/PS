import sys
def cal(a, b):
    A, B = a, b
    while a%b != 0:
        print(a, b)
        a, b = b, a%b

    print((A*B) // b)
T=int(sys.stdin.readline())
for i in range(T):
    A, B = map(int,sys.stdin.readline().split())
    cal(A,B)