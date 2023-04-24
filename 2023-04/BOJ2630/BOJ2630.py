# 2630번 색종이 만들기
# https://www.acmicpc.net/problem/2630
import sys, os
sys.stdin = open('{}/BOJ2630.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())
data = [sys.stdin.readline().strip().replace(" ", "") for i in range(N)]

white=0
blue=0

def devide(paper):
    if not paper:
        exit()
    global white
    global blue
    num=len(paper)
    half=num//2
    tmp2=paper[:half]
    tmp1=paper[half:]
    

        

    northWest=[]
    northEast=[]
    southWest=[]
    southEast=[]
    for item in tmp2:
        northEast.append(item[half:])
        northWest.append(item[:half])
    for item in tmp1:
        southEast.append(item[half:])
        southWest.append(item[:half])

    for item in [northWest, northEast, southWest, southEast]:
        if len(item)==1:
            if item.count('0')==0:
                blue+=1
            else:
                white+=1
            continue
            
        ans = [row.count('0') for row in item]
        if (ans.count(0) == half or ans.count(half)==half):
            if ans.count(0) == half:
                blue+=1
            else:
                white+=1
        else:
            devide(item)
            

ans = [row.count('0') for row in data]
if (ans.count(0) == N or ans.count(N)==N):
    if ans.count(0) == N:
        blue+=1
    else:
        white+=1
else:
    devide(data)


print(white)
print(blue)