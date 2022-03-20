import sys
S = int(sys.stdin.readline())
cnt=0
while(S>cnt):
    cnt+=1
    S-=cnt
print(cnt)