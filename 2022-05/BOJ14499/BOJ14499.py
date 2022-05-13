# 14499번 주사위 굴리기
# https://www.acmicpc.net/problem/14499
import sys, os
sys.stdin = open('{}/BOJ14499.txt'.format(os.path.dirname(os.path.realpath(__file__))))
class Dice:
    def __init__(self, x, y, M, N):
        self.top, self.bot, self.right, self.left, self.front, self.back = 0, 0, 0, 0, 0, 0
        self.x = x
        self.y = y
        self.maxX=M
        self.maxY=N
    def roll(self, num):
        if num==1:
            if self.x+1<self.maxX:
                self.x+=1
                self.top, self.right, self.bot, self.left = self.left, self.top, self.right, self.bot
                data[self.y][self.x]=self.paste(data[self.y][self.x])
                print(self.top)
        elif num==2:
            if self.x-1>=0:
                self.x-=1
                self.top, self.right, self.bot, self.left = self.right, self.bot, self.left, self.top
                data[self.y][self.x]=self.paste(data[self.y][self.x])
                print(self.top)
        elif num==3:
            if self.y-1>=0:
                self.y-=1
                self.top, self.back, self.bot, self.front = self.front, self.top, self.back, self.bot
                data[self.y][self.x]=self.paste(data[self.y][self.x])
                print(self.top)
        elif num==4:
            if self.y+1<self.maxY:
                self.y+=1
                self.top, self.back, self.bot, self.front = self.back, self.bot, self.front, self.top
                data[self.y][self.x]=self.paste(data[self.y][self.x])
                print(self.top)
       
    def paste(self, num):
        if num==0:
            return self.bot
        else:
            self.bot=num
            return 0
N, M, y, x, k=map(int,sys.stdin.readline().split())
dice=Dice(x, y, M, N)
data=[]
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))
p=list(map(int, sys.stdin.readline().split()))
for c in p:
    dice.roll(c)