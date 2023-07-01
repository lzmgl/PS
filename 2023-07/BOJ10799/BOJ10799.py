# 10799번 쇠막대기
# https://www.acmicpc.net/problem/10799
import sys, os
sys.stdin = open('{}/BOJ10799.txt'.format(os.path.dirname(os.path.realpath(__file__))))
data=sys.stdin.readline().strip()
arr=[]
ans=0
# 쇠막대랑 레이저 분리
data=data.replace("()", "0")
for c in data:
    if c=='(':
        arr.append(c)
    elif c==')': # 자투리 더해주기
        arr.pop()
        ans+=1
    else : # 레이저 잘릴때마다 쇠막대 갯수 더해주기
        ans+=len(arr)
print(ans)