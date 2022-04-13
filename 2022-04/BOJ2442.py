# 2442번 별 찍기 - 5
# https://www.acmicpc.net/problem/2442
N=int(input())
for i in range(1,N+1): 
    print(' '*(N-i), '*'*((i*2)-1), sep='')