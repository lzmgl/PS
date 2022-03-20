import sys
T = int(input())
while T>0:
    source = list(sys.stdin.readline().split())
    num = int(source[0])
    words = source[1]
    new_words=''
    for word in words:
        new_words+=word*num
    print(new_words)
    T-=1