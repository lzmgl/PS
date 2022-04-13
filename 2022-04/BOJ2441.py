# 2441번 별 찍기 - 4
# https://www.acmicpc.net/problem/2441
N=int(input())
for i in range(N,0,-1): 
    #print(('*'*i).rjust(N))
    print(f'{"*"*i:>{N}}')