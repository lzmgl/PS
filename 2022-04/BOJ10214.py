import sys
T = int(sys.stdin.readline())
for _ in range(T):
    Y=K=0
    for _ in range(9):
        a,b = map(int, sys.stdin.readline().split())
        Y+=a
        K+=b
    print('Yonsei' if Y>K else 'Korea' if K>Y else 'Draw' )