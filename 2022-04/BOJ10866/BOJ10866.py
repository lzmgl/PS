# 10866번 덱
# https://www.acmicpc.net/problem/10866
import sys, os
    
sys.stdin = open('{}/BOJ10866.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
data=[]
for _ in range(N):
    oper=sys.stdin.readline().strip().split()
    if 'push_front' in oper[0]:
        data.insert(0,int(oper[1]))
    elif 'push_back' in oper[0]:
        data.append(int(oper[1]))
    elif 'pop_front' in oper:
        try:
            print(data.pop(0))
        except:
            print(-1)
    elif 'pop_back' in oper:
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
    elif 'front' in oper:
        try:
            print(data[0])
        except:
            print(-1)
    elif 'back' in oper:
        try:
            print(data[len(data)-1])
        except:
            print(-1)
    