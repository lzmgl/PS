import sys
n=int(sys.stdin.readline())
data = list(sys.stdin.readline().strip().split())
m=int(sys.stdin.readline())

is_p = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n+1):
    is_p[i][i] = 1

for i in range(1, n):
    if data[i-1] == data[i]:
        is_p[i][i+1] = 1

for i in range(2, n):
    for j in range(1, n+1-i):
        if data[j-1] == data[j+i-1] and is_p[j+1][i+j-1] == 1:
            is_p[j][i+j] = 1

for i in range(1,m+1):
    s, e = map(int, sys.stdin.readline().split())
    print(is_p[s][e])