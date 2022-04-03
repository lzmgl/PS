import sys
a = input()
b=input()
c=input()
if b=='*':
    print(a+c[1:])
else:
    if a==c:
        print(int(a)+int(c))
        exit()
    c='0b'+c
    a='0b'+a
    print(str(bin(int(a,2)+int(c,2)))[2:])