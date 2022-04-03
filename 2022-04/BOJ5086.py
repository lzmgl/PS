while (s:=input())>'0 0':
    a,b=map(int,s.split(' '))
    if a%b==0:
        print("multiple")
    elif b%a==0:
        print("factor")
    else:
        print("neither")
'''
while a:a,b=map(int, input().split())