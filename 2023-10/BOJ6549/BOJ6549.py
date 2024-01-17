# 6549번 히스토그램에서 가장 큰 직사각형
# https://www.acmicpc.net/problem/6549
import sys, os
sys.stdin = open('{}/BOJ6549.txt'.format(os.path.dirname(os.path.realpath(__file__))))
while True:
    data = list(map(int,sys.stdin.readline().split()))
    if data[0]==0:
        break
    stack=[]
    maxN=0
    for i,h in enumerate(data):
        if i==0:
            continue
        
        if stack and stack[-1][0]>h:
            while stack:
                height, idx = stack.pop()
                width=1
                if stack:
                    width=stack[-1][1]+1
                ans = (i - width) * height
                maxN=max(maxN, ans)
                if not stack or stack[-1][0] <= h:
                    break
        if not stack or stack[-1][0]<=h:
            stack.append((h,i))
        
    while stack:
        height, idx = stack.pop()
        width=1
        if stack:
            width=stack[-1][1]+1
        ans = (data[0]+1 - width) * height
        maxN=max(maxN, ans)
    print(maxN)
            