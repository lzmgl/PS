# 9375번 패션왕 신해빈
# https://www.acmicpc.net/problem/9375
import sys, os
sys.stdin = open('{}/BOJ9375.txt'.format(os.path.dirname(os.path.realpath(__file__))))
T=int(sys.stdin.readline().strip())
for _ in range(T):
    answer=1
    ans=dict()
    N=int(sys.stdin.readline().strip())
    if N==0:
        print(0)
        continue
    for _ in range(N):
        tmp = sys.stdin.readline().split()
        if tmp[1] in ans:
            ans[tmp[1]]=(','.join(ans[tmp[1]])+','+tmp[0]).split(',')
        else:
            ans[tmp[1]]= [tmp[0]]
    for item in ans:
        answer*=(len(ans[item])+1)
    answer-=1
    print(answer)
