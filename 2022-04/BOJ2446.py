# 2446번 별 찍기 - 8
# https://www.acmicpc.net/problem/2446
N=int(input())
for i in range(-N+1,N):
    i=abs(i)
    print(' '*(N-i-1), '*'*(2*(i)+1),sep='')