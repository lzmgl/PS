import sys
x=0
y=0
for i in range(3):
    a1, b1 = map(int,sys.stdin.readline().split())
    x^=a1
    y^=b1
print(x,y)