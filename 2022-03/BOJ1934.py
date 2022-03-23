import sys
def cal(a, b):
    A, B = a, b
    while a%b != 0:
        a, b = b, a%b
    print((A*B) // b)
for _ in[0]*int(input()):
    A, B = map(int,sys.stdin.readline().split())
    cal(A,B)
    