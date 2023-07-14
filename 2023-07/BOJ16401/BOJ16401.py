# 16401번 과자 나눠주기
# https://www.acmicpc.net/problem/16401
import sys, os
sys.stdin = open('{}/BOJ16401.txt'.format(os.path.dirname(os.path.realpath(__file__))))
def cut(data_list, h):
    sumN=0
    for item in data_list:
        sumN+=item//h

    return sumN

def binarySearch(left, right, data, m):
    while left<=right:
        mid=(left+right)//2
        if cut(data, mid)>=m:
            left=mid+1
        else:
            right=mid-1
    return right

m,n=map(int,sys.stdin.readline().split())
data=list(map(int, sys.stdin.readline().split()))
data.sort()
print(binarySearch(1, data[-1], data, m))