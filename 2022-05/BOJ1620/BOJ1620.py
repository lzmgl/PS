# 1620번 나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620
import sys, os
sys.stdin = open('{}/BOJ1620.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N, M=map(int,sys.stdin.readline().split())
data={}
for i in range(N):
    tmp = (sys.stdin.readline().strip())
    data[i]=tmp
    data[tmp]=i
for _ in range(M):
    tmp=(sys.stdin.readline().strip())
    try:
        tmp = int(tmp)-1
        print(data[tmp])
    except:
        i = (data[tmp])
        print(i+1)