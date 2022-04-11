'''
N=int(input())
for i in range(1,N): 
    print(' '*(N-i), '*'*((i*2)-1), sep='')
for i in range(N,0,-1): 
    print(' '*(N-i), '*'*((i*2)-1), sep='')
'''
N=int(input())
for i in range(-N+1,N): 
    i=abs(i)
    print(' '*(i), '*'*(2*(N-i)-1), sep='')