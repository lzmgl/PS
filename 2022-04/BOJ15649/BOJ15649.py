# 15649번 N과 M (1)
# https://www.acmicpc.net/problem/15649
import sys, os
    
sys.stdin = open('{}/BOJ15649.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N,M=map(int,sys.stdin.readline().split())
s=[]
def DFS():
    if len(s)==M:
        print(*s)
    else:
        for i in range(1, N+1):
            if i not in s:
                s.append(i)
                DFS()
                s.pop()
                
DFS()