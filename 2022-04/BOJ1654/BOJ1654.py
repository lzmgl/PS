# 1654번 랜선 자르기
# https://www.acmicpc.net/problem/1654
import sys, os
    
sys.stdin = open('{}/BOJ1654.txt'.format(os.path.dirname(os.path.realpath(__file__))))
K, N=map(int,sys.stdin.readline().split())
lanCable = [int(sys.stdin.readline()) for _ in range(K)]
tmp=0
def binary_search(v, l, r):
    global tmp
    cnt=0
    if l>r:
        return 0
    mid=(l+r)//2
    for i in lanCable:
        cnt+=i//mid
    if cnt>=v:
        if mid>tmp:
            tmp=mid
        return binary_search(v, mid+1, r)
    elif cnt<v:
        return binary_search(v, l, mid-1)

lanCable.sort()
binary_search(N, 1, lanCable[K-1])
print(tmp)