# 1296번 팀 이름 정하기
# 구현
# https://www.acmicpc.net/problem/1296
import sys, os
sys.stdin = open('{}/BOJ1296.txt'.format(os.path.dirname(os.path.realpath(__file__))))
s=(sys.stdin.readline().strip())
L1=s.count('L')
O1=s.count('O')
V1=s.count('V')
E1=s.count('E')
n=int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
data.sort()
maxN=0
maxS=''
for s in data:
    L=s.count('L')+L1
    O=s.count('O')+O1
    V=s.count('V')+V1
    E=s.count('E')+E1
    cnt=(((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100)
    if cnt>maxN:
        maxS=s
        maxN=cnt
if not maxS:
    maxS=data[0]
print(maxS)