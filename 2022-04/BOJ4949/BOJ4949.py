# 4949번 균형잡힌 세상
# stack 스택 입력개행
# https://www.acmicpc.net/problem/4949
import sys, os
sys.stdin = open('{}/BOJ4949.txt'.format(os.path.dirname(os.path.realpath(__file__))))
s=sys.stdin.readline()
while s != '.' or s!='.\n':
    # print(s)
    stack=[]
    bal=True
    try:
        for c in s:
            if c=='(':
                stack.append(c)
            elif c==')':
                tmp=stack.pop()
                if tmp!='(':
                    bal=False
                    print('no')
                    break
            if c=='[':
                stack.append(c)
            elif c==']':
                tmp=stack.pop()
                if tmp!='[':
                    bal=False
                    print('no')
                    break
    except:
        bal=False
        print('no')
    # print(len(stack))
    if bal:
        if len(stack) ==0:
            print('yes')
        else:
            print('no')
    s=sys.stdin.readline()
    if s == '.' or s=='.\n':
        break