# 1351번 무한 수열
# https://www.acmicpc.net/problem/1351
import sys, os
sys.stdin = open('{}/BOJ1351.txt'.format(os.path.dirname(os.path.realpath(__file__))))
from collections import defaultdict
N, P, Q=map(int,sys.stdin.readline().split())
# 메모이제이션 = 메모리 초과 (10^^12)
# ans=[0]*100000000001
# ans[0]=1
# print('A[0]')
# for i in range(1,100000000001):
#     ans[i]=ans[i//P]+ans[i//Q]
#     print(f'A[{i}] = A[{i//P}] + A[{i//Q}]')
# print(ans[N])
ans = defaultdict(int)
ans[0]=1
def dfs(n):
    if ans[n]!=0:
        return ans[n]
    ans[n] = dfs(n//P) + dfs(n//Q)
    return ans[n]

print(dfs(N))
