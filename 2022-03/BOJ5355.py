import sys
T = int(input())
outputlist=[]
while T>0:
    source = list(sys.stdin.readline().split())
    l = len(source)
    num = float(source[0])
    i=1
    while i!=l:
        if source[i] == '@':
            num*=3
        elif source[i] == '%':
            num+=5
        else :
            num-=7
        i+=1
    T-=1
    outputlist.append(f'{num:.2f}')
print(*outputlist, sep='\n')