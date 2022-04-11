N=int(input())
for i in range(-N+1,N):
    i=abs(i)
    print(' '*(N-i-1), '*'*(2*(i)+1),sep='')