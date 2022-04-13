# 1920번 수 찾기
# 이진탐색
# 미해결
# https://www.acmicpc.net/problem/1920
import sys
N=int(sys.stdin.readline())
dataN=list(map(int,sys.stdin.readline().rstrip().split()))
M=int(sys.stdin.readline())
dataM=list(map(int,sys.stdin.readline().rstrip().split()))

def binarySearch(v, l, r):
    if l>r or l<0 or r>M-1:
        return 0
    mid=(l+r)//2
    if v==dataN[mid]:
        return 1
    elif v<dataN[mid]:
        return binarySearch(v, l, mid-1)
    else:
        return binarySearch(v, mid+1, r)
dataN.sort()
for itemM in dataM:
    print(binarySearch(itemM,0,M-1))