# 10828번 스택
# https://www.acmicpc.net/problem/10828
import sys, os
    
sys.stdin = open('{}/BOJ10828.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
data=[]
for _ in range(N):
    oper=sys.stdin.readline().strip().split()
    if len(oper)>1:
        data.append(int(oper[1]))
    elif 'pop' in oper:
        try:
            print(data.pop())
        except:
            print(-1)
    elif 'size' in oper:
        print(len(data))
    elif 'empty' in oper:
        if len(data)>0:
            print(0)
        else:
            print(1)
    else:
        try:
            print(data[len(data)-1])
        except:
            print(-1)
    