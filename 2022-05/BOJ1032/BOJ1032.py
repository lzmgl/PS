# 1032번 명령 프롬프트
# https://www.acmicpc.net/problem/1032
import sys, os
sys.stdin = open('{}/BOJ1032.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
data=[]
for _ in range(N):
    data.append(sys.stdin.readline().strip())
ans=''
for i,c in enumerate(data[0]):
    isDifference=False
    for j in range(N):
        if c != data[j][i]:
            isDifference=True
    if isDifference:
        ans+='?'
    else:
        ans+=c
print(ans)
    