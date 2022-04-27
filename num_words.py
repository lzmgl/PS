import os, sys
sys.stdin = open('b.txt'.format(os.path.dirname(os.path.realpath(__file__))))
words = sys.stdin.readlines()
cnt=0
for sentence in words:
    for c in sentence:
        if c != ' ' and c != '\n':
            cnt+=1

print(cnt-57)