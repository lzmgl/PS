import sys
side = {'Q1':0, 'Q2':0, 'Q3':0, 'Q4':0, 'AXIS':0}
N=int(sys.stdin.readline())
for _ in range(N):
    x,y=map(int, sys.stdin.readline().split())
    if x>0:
        if y>0:
            side['Q1']+=1
        elif y<0:
            side['Q4']+=1
        else:
            side['AXIS']+=1
    elif x<0:
        if y>0:
            side['Q2']+=1
        elif y<0:
            side['Q3']+=1
        else:
            side['AXIS']+=1
    else:
        side['AXIS']+=1
for key, value in side.items():
    print(key+': '+str(value))