import sys
N=int(sys.stdin.readline())
appleSum=0
for _ in range(N):
    studentNum, apple = map(int, sys.stdin.readline().split())
    appleSum+=apple%studentNum
print(appleSum)