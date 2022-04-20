# 15650번 N과 M (2)
# https://www.acmicpc.net/problem/15650
import sys, os
    
sys.stdin = open('{}/BOJ15650.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N,M=map(int,sys.stdin.readline().split())
s=[x for x in range(1, N+1)]

print(s)
visited=[]
def DFS(arr, n):
    if len(visited)==n:
        print(visited)
    else:
        for i in range(1, n+1):
            visited.append(i)
            DFS()
            visited.pop()
DFS([], M)