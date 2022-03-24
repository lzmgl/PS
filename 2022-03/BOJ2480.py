'''
import sys
import math
A, B, C = map(int, sys.stdin.readline().split())
if A==B==C:
    print(10000+A*1000)
elif A!=B and A!=C and B!=C:
    print(max(A,B,C)*100)
else :
    if A==B:
        print(1000+A*100)
    elif A==C:
        print(1000+A*100)
    else:
        print(1000+B*100)
'''

*_,a,b,c=sorted(input())
print(a,b,c)
print(['1'+b,c])
print([a<b<c])
print('000'[a<c:])
print(['1'+b,c][a<b<c]+'000'[a<c:])
print([a,b][False])
