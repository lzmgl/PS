# 1920번 수 찾기
# https://www.acmicpc.net/problem/1920
import sys, os
sys.stdin = open('{}/BOJ1920.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 1920번 수 찾기
# 이진탐색
# 존재만 탐색하면 되기때문에 set 사용..
# https://www.acmicpc.net/problem/1920
import sys
N=int(sys.stdin.readline())
dataN=set(map(int,sys.stdin.readline().rstrip().split()))
M=int(sys.stdin.readline())
dataM=list(map(int,sys.stdin.readline().rstrip().split()))
'''
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
'''
for itemM in dataM:
    print('1' if itemM in dataN else '0')