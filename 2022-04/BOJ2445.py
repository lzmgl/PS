N=int(input())
for i in range(-N+1,N):
    i=abs(i)
    print('*'*(N-i), ' '*(i*2), '*'*(N-i),sep='')