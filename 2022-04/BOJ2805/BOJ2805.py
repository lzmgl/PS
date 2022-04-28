# 2805번 나무 자르기
# 이분 탐색 매개 변수 탐색
# https://www.acmicpc.net/problem/2805
import sys, os
sys.stdin = open('{}/BOJ2805.txt'.format(os.path.dirname(os.path.realpath(__file__))))

def cut(data_list, h):
    sumN=0
    for item in data_list:
        tmp=item-h
        if tmp>0:
            sumN+=tmp
    return sumN


def binarySearch(v, l, r, data):
    if l>r or l<0:
        return r
    mid=(l+r)//2
    if v==cut(data, mid):
        return mid
    elif v<cut(data, mid):
        return binarySearch(v, mid+1, r, data)
    else:
        return binarySearch(v, l, mid-1, data)

N, M=map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
h=0
h=binarySearch(M, 0, data[N-1], data)
print(h)