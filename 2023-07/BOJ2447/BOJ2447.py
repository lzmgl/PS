# 2447번 별 찍기 - 10
# https://www.acmicpc.net/problem/2447
import sys, os
sys.stdin = open('{}/BOJ2447.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
def star(n):
    sp=n//3
    if sp==1:
        return ['***','* *','***']
    else:
        return [i*3 for i in star(sp)]+[i+sp*' '+i for i in star(sp)]+[i*3 for i in star(sp)]
answer=star(N)
print(*answer, sep='\n')