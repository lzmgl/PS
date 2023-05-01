# 1208번 부분수열의 합 2
# https://www.acmicpc.net/problem/1208
import sys, os
sys.stdin = open('{}/BOJ1208.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, S=map(int,sys.stdin.readline().split())
from bisect import bisect_left, bisect_right
from itertools import combinations
data=list(map(int, sys.stdin.readline().split()))
def getNum(arr, find):
    print(bisect_right(arr, find))
    print(bisect_left(arr, find))
    return bisect_right(arr, find) - bisect_left(arr, find)

m = N//2
n = N - m    
first = [0]*(1<<n)
second = [0]*(1<<m)
# getSum(left, first)
# getSum(right, second)

# 비트마스킹을 이용하여 Subset의 합을 담는다
for i in range(1<<n):
    for k in range(n):
        if (i&(1<<k)) > 0:
            first[i] += data[k]
            
# second : 오른쪽 Subset
second = [0]*(1<<m)
for i in range(1<<m):
    for k in range(m):
        if (i&(1<<k)) > 0:
            second[i] += data[k+n]
            

print(first, second)
ans=0

for l in first:
    f=S-l
    ans+=getNum(second, f)
    print(ans)
print(ans)
ans+=getNum(first, S)
ans+=getNum(second, S)


print(ans)