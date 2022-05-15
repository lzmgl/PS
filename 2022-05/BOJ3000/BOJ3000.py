# 3000번 직각 삼각형
# https://www.acmicpc.net/problem/3000
import sys, os

sys.stdin = open('{}/BOJ3000.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
data=[]
xspot=[0]*100001
yspot=[0]*100001
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    data.append([x,y])
    xspot[x]+=1
    yspot[y]+=1

res=0
for i in range(N):
    if xspot[data[i][0]]>1 and yspot[data[i][1]]>1:
        res+=(xspot[data[i][0]]-1)*(yspot[data[i][1]]-1)
print(res)