import sys
from collections import defaultdict
n=int(sys.stdin.readline())
cnt=0
s=defaultdict()
for _ in range(n):
    tmp=sys.stdin.readline().rstrip()
    if tmp !='ENTER':
        if tmp not in s:
            s[tmp]=0
            cnt+=1
    else:
        s=defaultdict()
print(cnt)