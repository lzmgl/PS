# 17219번 비밀번호 찾기
# https://www.acmicpc.net/problem/17219
import sys, os
sys.stdin = open('{}/BOJ17219.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, M = map(int,sys.stdin.readline().split())
data={}
for _ in range(N):
    adr, pwd = sys.stdin.readline().split()
    data[adr]=pwd
ans=[ sys.stdin.readline().strip() for _ in range(M) ]

for item in ans:
    print(data[item])