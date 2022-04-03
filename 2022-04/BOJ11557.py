import sys
T = int(sys.stdin.readline())
for _ in range(T):
    maxNum=0
    res=''
    N = int(sys.stdin.readline())
    for _ in range(N):
        name, amount = sys.stdin.readline().split()
        if int(amount)>=maxNum:
            maxNum=int(amount)
            res=name
    print(res)