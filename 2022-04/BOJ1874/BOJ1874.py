# 1874번 스택 수열
# https://www.acmicpc.net/problem/1874
import sys, os
    
sys.stdin = open('{}/BOJ1874.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
st = [int(sys.stdin.readline()) for _ in range(N)]
'''
height=0
maxH=0
for i in range(N):
    height=compStack[i]
    if maxH<=height:
        for _ in range(height-maxH):
            print('+')
        print('-')
        maxH=max(compStack[i], maxH)
    if height<maxH:
        print('-')
'''

data=[0]
res=[]
idx=0
i=1 # data 1부터 입력됨
# stack idx loop
while idx<N:
    if data[-1]<st[idx]: # data pop값 != stack[idx]
        res.append('+')
        data.append(i)
        i+=1
    elif data[-1]==st[idx]: # data pop == stack[idx]
        res.append('-')
        data.pop()
        idx+=1
        if idx>=N:
            break
    else:
        print('NO')
        exit()
for item in res:
    print(item)
'''
data=[-2]
res=[]
idx=0
i=1
print(st)
while idx<N:
    if data[-1]!=st[idx]:
        res.append('+')
        data.append(i)
        i+=1
    else:
        res.append('-')
        data.pop()
        idx+=1
        if idx>=N:
            break
    if data[-1]>st[idx]:
        print('NO')
        exit()
for item in res:
    print(item)
'''




'''
data=[]
print(compStack)
idx=0
stackidx=0
res=[]
maxN=1
i=1
while i<N+1:
    print(f'compStack={compStack[idx]}')
    if i<=compStack[idx]:
        print(f'push {i}')
        maxN=max(maxN, i)
        data.append(i)
        res.append('+')
    else:
        
    if data[-1]==compStack[idx]:
        print(f'pop {compStack[idx]}')
        data.pop()
        res.append('-')
        idx+=1
        i-=1
        print(f'i={i}')
    i+=1
print(data)
print(res)
'''