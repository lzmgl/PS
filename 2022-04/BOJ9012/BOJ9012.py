# 9012번 괄호
# https://www.acmicpc.net/problem/9012
import sys, os
sys.stdin = open('{}/BOJ9012.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())# 9012번 괄호
# https://www.acmicpc.net/problem/9012
import sys
N=int(sys.stdin.readline())
'''
for _ in range(N):
    tmp=sys.stdin.readline().rstrip()
    cnt=0
    for c in tmp:
        if c=='(':
            cnt+=1
        else:
            cnt-=1
            if cnt<0:
                break
    if cnt==0:
        print('YES')
    else:
        print('NO')

'''

for _ in range(N):
    tmp=sys.stdin.readline().rstrip()
    ans=[]
    for c in tmp:
        if c=='(':
            ans.append(c)
        else:
            try:
                ans.pop()
            except:
                ans.append(c)
                break
    if ans:
        print('NO')
    else:
        print('YES')