import sys
N=int(sys.stdin.readline())
zero=[]
one=[]
for i in range(41):
    zero.append(0)
    one.append(0)
zero[0], zero[1] =1, 0
one[0], one[1]= 0, 1
for i in range(2,41):
    zero[i] = zero[i-1] + zero[i-2]
    one[i] = one[i-1] + one[i-2]
    
for _ in range(N):
    n=int(sys.stdin.readline())
    print(zero[n], one[n])
    