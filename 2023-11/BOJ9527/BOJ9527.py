import sys
import math

sys.setrecursionlimit(10**8)
a,b = map(int, sys.stdin.readline().split())

def sol(x):
    if x<=0:
        return 0
    po=int(math.log2(x))
    tmp=2**po
    if tmp==x:
        return po*x//2+1
    distance=x-tmp
    return sol(tmp)+distance+sol(distance)

print(sol(b)-sol(a-1))