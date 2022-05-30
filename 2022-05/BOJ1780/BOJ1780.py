# 1780번 종이의 개수
# https://www.acmicpc.net/problem/1780
import sys, os
sys.stdin = open('{}/BOJ1780.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
m=0
z=0
p=0
def solve(x, y, n):
    global m, z, p
    check = data[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if data[i][j]!=check:
                for k in range(3):
                    for l in range(3):
                        solve(x+k*n//3, y+l*n//3, n//3)
                return
    if check==-1:
        m+=1
    elif check == 0:
        z+=1
    else:
        p+=1
solve(0, 0, N)
print(m)
print(z)
print(p)