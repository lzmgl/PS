# 2445번 별 찍기 - 8
# https://www.acmicpc.net/problem/2445
N=int(input())
for i in range(-N+1,N):
    i=abs(i)
    print('*'*(N-i), ' '*(i*2), '*'*(N-i),sep='')