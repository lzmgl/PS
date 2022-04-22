# 13458번 시험 감독
# https://www.acmicpc.net/problem/13458
import sys, os
    
sys.stdin = open('{}/BOJ13458.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
A_list=list(map(int,sys.stdin.readline().split()))
B, C=map(int,sys.stdin.readline().split())
cnt=0
for room in A_list:
    cnt+=1
    if room > B:
        room-=B
        cnt += room//C
        if room%C != 0:
            cnt +=1
print(cnt)