import sys
N=int(sys.stdin.readline())
for i in range(N):
    V, E = map(int, sys.stdin.readline().split())
    print(2-V+E)