# 11723번 집합
# https://www.acmicpc.net/problem/11723
import sys, os
sys.stdin = open('{}/BOJ11723.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
ans=set()
for i in range(N):
    item = sys.stdin.readline().strip().split(" ")
    if len(item)==1:
        if item[0]=='all':
            ans=set([x for x in range(1,21)])
        else:
            ans.clear()
        continue
    tar=int(item[1])
    if item[0]=='add':
        ans.add(tar)
    elif item[0]=='remove':
        ans.discard(tar)
    elif item[0]=='check':
        print(1 if tar in ans else 0)
    elif item[0]=='toggle':
        if tar in ans:
            ans.discard(tar)
        else:
            ans.add(tar)