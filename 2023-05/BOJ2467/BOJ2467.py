# 2467번 용액
# https://www.acmicpc.net/problem/2467
import sys, os
sys.stdin = open('{}/BOJ2467.txt'.format(os.path.dirname(os.path.realpath(__file__))))
import math
N=int(sys.stdin.readline())
data=list(map(int, sys.stdin.readline().split()))
data.sort()
t1, t2 = 0, 0
_min=math.inf
target=0
for i in range(N):
        
    start=i+1
    end=N-1
    while start <= end:
        mid = (start + end) // 2
        result = data[i]+data[mid]

        if abs(result) <= abs(_min):
            t1, t2  = data[i], data[mid]
            _min = result

        if  result == target:
            t1, t2  = data[i], data[mid]
            print(t1, t2)
            exit()
        elif result < target:
            start = mid + 1
        else:
            end = mid -1

print(t1,t2)